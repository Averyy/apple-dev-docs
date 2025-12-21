# Developing a browser app that uses an alternative browser engine

**Framework**: BrowserEngineKit

Create a web browser app and associated extensions.

**Availability**:
- iOS 17.4+
- Xcode 15.3+

#### Overview

This sample code project demonstrates how a web browser app uses [`BrowserEngineKit`](BrowserEngineKit.md) and [`XPC`](https://developer.apple.com/documentation/XPC) to communicate with its alternative browser engine over XPC, and implement a browser UI. The workspace contains four targets that define components of the browser app:

- `BrowserExample` contains the main app that presents the UI.
- `RenderingExtension` contains the rendering extension that the app uses to play media and render complex views.
- `NetworkingExtension` contains the networking extension that the app uses to fetch data from remote websites.
- `WebContentExtension` contains the web content extension that the app uses to parse HTML content and compile code just-in-time.

For more information on how these targets work together to support a custom web browser engine, see [`Designing your browser architecture`](designing-your-browser-architecture.md).

##### Configure the Sample Code Project

To build a web browser that uses an alternative browser engine, including the one in this sample project, apply for the entitlements from Apple. The entitlement request process varies by region:

For more information on which entitlements to use, see [`Creating browser extensions in Xcode`](creating-browser-extensions-in-xcode.md).

To build the sample code project for a device, you must target an iPhone that supports the `arm64e` instruction set. The project doesn’t support iPad.

##### Open a New Tab

When someone using the browser app opens a new tab, the browser app’s `BrowserPage` creates a `TabContentView` to display the tab’s contents, which gets its data from the tab’s `TabViewModel`.

```swift
struct TabContentView: View {
  
  @ObservedObject var tab: TabViewModel
  
  var body: some View {
    if let error = tab.error {
      VStack {
        Image(systemName: "exclamationmark.triangle")
        Text(error.localizedDescription)
      }
    } else {
      WebViewRepresentable(webView: tab.webView)
    }
  }
}
```

The `TabViewModel`‘s `webView` property is a `WebView` that displays the tab’s contents, which the `TabContentView` wraps in a `WebViewRepresentable` to display using SwiftUI.

The `WebView`’s initializer creates a `WebContentView`, which is the view that renders the HTML document in the tab. `WebContentView` calls `launchProcesses(id: PageID)`, which does the following:

- Creates a new web content extension process to render the web content, and set up an XPC connection between the browser app and the web content process.

```None
    let contentProcess = try await getOrLaunchContentProcess(pageID: id)
    let contentConnection = try contentProcess.makeLibXPCConnection()
    let contentProxy = WebContentExtensionProxy(connection: contentConnection)
    try contentProxy.lockdown(version: lockdownVersion)
```

- Gets a connection to the single rendering-extension process, launching it if necessary.

```None
    let renderingProcess = try await getOrLaunchRenderingProcess()
    let renderingConnection = try renderingProcess.makeLibXPCConnection()
    let renderingProxy = RenderingExtensionProxy(connection: renderingConnection)
```

- Asks the rendering process to create an anonymous XPC connection and sends an endpoint for the connection to the browser app.

```None
    let renderingEndpoint = try await renderingProxy.getEndpoint()
```

- Repeats steps 2-3 for the single networking extension process, so that the browser app has an anonymous XPC connection endpoint for the networking process.

```None
    let networkProcess = try await getOrLaunchNetworkProcess()
    let networkConnection = try networkProcess.makeLibXPCConnection()
    let networkProxy = NetworkingExtensionProxy(connection: networkConnection)
    let networkEndpoint = try await networkProxy.getEndpoint()
```

- Sends a bootstrap message to the web-content process, handing it the endpoints to the other two extension processes, so that they can communicate directly.

```None
    try await contentProxy.bootstrap(renderingExtension: renderingEndpoint, networkExtension: networkEndpoint)
```

The web content process responds to the bootstrap message by retrieving the anonymous XPC connections for the other extensions from the endpoints it was sent by the host app, and sends them each “ping” messages to ensure the connections are valid.

```None
  private func perform(bootstrap cmd: WebContentExtensionBootstrapCommand) async throws {
    log.log("performing bootstrap")
    
    if let renderingProxy = self.renderingProxy { // Connect to the Rendering extension if needed
      log.log("already connected to rendering extension: \(String(describing: renderingProxy.connection))")
    } else {
      let endpoint = cmd.renderingEndpoint
      log.log("connecting to rendering extension at: \(String(describing: endpoint))")
      let connection = xpc_connection_create_from_endpoint(endpoint)
      self.renderingProxy = .init(connection: connection)
      try await connection.ping()
      log.log("connected to rendering extension: \(String(describing: connection))")
    }
    
    if let networkProxy = self.networkProxy {  // Connect to the Networking extension if needed
      log.log("already connected to network extension: \(String(describing: networkProxy.connection))")
    } else {
      let endpoint = cmd.networkEndpoint
      log.log("connecting to network extension at: \(String(describing: endpoint))")
      let connection = xpc_connection_create_from_endpoint(endpoint)
      self.networkProxy = .init(connection: connection)
      try await connection.ping()
      log.log("connected to network extension: \(String(describing: connection))")
    }
  }
```

For more information on this process, see the section “Pass anonymous connection endpoints between extensions” in [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

##### Load Web Content

When someone using the browser app navigates to a new location, the `WebContentView` asks the proxy object that represents the web-content process to load the data at the location’s URL:

```None
    let result = try await webContentProxy.load(destination: destination)
```

This method sends a network load message to the web-content process:

```None
    let task: WebContentExtensionTask = .load(destination: destination)
    return try await connection.sendWithReply(task, decodingReplyAs: NetworkTaskResult.self)
```

The web-content process checks what kind of data it’s trying to load. If it’s a URL, it asks the networking extension to load the content. Otherwise, it prepares the data itself, either by decoding a string, or loading the contents of a file.

```None
    switch destination {
    case .url(let url):
      guard let networkProxy else {
        throw CustomBrowserError("not connected to the network extension")
      }
      return try await networkProxy.fetchData(from: url)
    case .htmlString(let string):
      guard let data = string.data(using: .utf8) else {
        throw CustomBrowserError("failed to get utf8 data from string")
      }
      return .init(response: nil, data: data, error: nil)
    case .localFile(let file):
      let data = try Data(contentsOf: file)
      return .init(response: nil, data: data, error: nil)
    }
```

> **Note**:  To open a file in your browser, send a bookmark with implicit security scope to the web-content process, so that it can extend its sandbox to access the file. For more information, see [`Accessing files in browser extensions`](accessing-files-in-browser-extensions.md).

In your browser app, you need to handle any networking errors at this point. If the networking extension loads the content, parse it using your alternative browser engine to create rendering commands, that you send to the rendering process. In the rendering process, update the layer that the browser app is hosting.

Finally, the web-content process replies to the browser app, telling the `WebContentView` to update its view.

```None
    render(result)
```

## See Also

- [Designing your browser architecture](designing-your-browser-architecture.md)
  Isolate privileged access to operating system resources and private data from untrusted code.
- [Preparing your app to be the default web browser](../Xcode/preparing-your-app-to-be-the-default-browser.md)
  Configure your browser app so users can set it as the default on their device instead of Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/developing-a-browser-app-that-uses-an-alternative-browser-engine)*