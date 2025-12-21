# Adding support for app extensions to your app

**Framework**: ExtensionFoundation

Create an app extension model by defining your code’s extension points and communicating with app extensions at runtime.

#### Overview

App extensions are a way to extend your app’s features safely, using code that runs in a separate process. An app extension is a bundle that’s separate from your app but contains code that works in tandem with that app. A productivity app might use app extensions to run potentially risky code in an isolated process, rather than in the app itself. An app might also use app extensions to incorporate new capabilities from external developers. For example, a video editing app might allow developers to create their own filters or tools and integrate them into the video editing workflow.

The host app determines when to run an app extension, and defines the API that both it and the app extension use to communicate. Apps use the [`ExtensionFoundation`](ExtensionFoundation.md) framework to launch app extensions and start them running in a separate process. Apps also use the framework to establish an XPC connection to an app extension, which allows the two processes to communicate with each other. App extensions similarly use the framework to start up and respond to XPC connection requests.

##### Define an Api for Shared Communication

Communication between an app and its app extensions occurs through well-defined interfaces that the app’s creator defines. When adding support for app extensions to your app, consider what features you want those extensions to support. Build APIs around specific features and launch app extensions that implement those APIs. For example, an image-editing app might define an API to manipulate the contents of an image. Typically, you define your API using protocols, but you can define other types too.

The APIs you define must be interoperable with the XPC technology that the app and app extension use to communicate. The [`ExtensionFoundation`](ExtensionFoundation.md) framework lets you create an XPC connection using [`XPC`](https://developer.apple.com/documentation/Foundation/xpc) or types from the lighter-weight [`XPC`](https://developer.apple.com/documentation/XPC) framework. Both technologies offer similar features, but the XPC framework is a better option for exchanging data with an app extension running in a hardened sandbox. For additional information about how to build your custom APIs to support XPC, see the documentation for those technologies.

##### Define Your Apps Extension Points in Code

Apps define extension points to ensure that the app extensions they launch are capable of performing the correct tasks. An extension point corresponds to one of the app’s features, and you define it by assigning a name and other relevant attributes. For example, you might define an extension point for modifying the contents of an image. Host apps define their extension points in code using [`ExtensionFoundation`](ExtensionFoundation.md) types, which the compiler turns into an `.appext` file that ships inside the app’s bundle. The system uses the contents of that file to locate matching app extensions.

An app may define multiple extension points, but each app extension supports only one extension point. An app might use different extension points to support different features. For example, a video editing app might use one extension point for video filters and a different extension point for file exporters. When defining each extension point, consider the interaction model between your app and the app extensions and add any attributes that apply:

-  App extensions can do work with or without providing a custom UI. If an extension point requires a UI, the app and app extensions must also adopt the [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework, and use that framework to present the UI.
-  If an app extension processes unknown data or handles external input, you can choose to run it in a restrictive sandbox to minimize any potential damage from malicious code. The system requires app extensions to have specific sandbox-related entitlements.
-  You might choose to run app extensions that reside anywhere in the system, or that reside only inside your app’s bundle. Extension points adopt the bundle-only approach by default, but you can use this attribute to allow external developers to contribute app extensions.

Define your app’s extension points programmatically using the [`AppExtensionPoint.Definition`](appextensionpoint/definition.md) property wrapper. In your app’s code, extend the [`AppExtensionPoint`](appextensionpoint.md) type and add a static variable with your extension point definition. Add the [`AppExtensionPoint.Name`](appextensionpoint/name.md) attribute and any other attributes relevant for your extension point. The following example creates a minimal extension point without any UI or enhanced security:

```swift
extension AppExtensionPoint {
    @Definition
    public static var myExtensionPoint: AppExtensionPoint {
        Name("MyExtensionPoint")
    }
}
```

To add additional attributes, add them to your extension point definition. The following example creates an extension point for an app that displays custom greetings. The scope attribute opens up the extension point to app extensions anywhere on the system.

```swift
extension AppExtensionPoint {
    @Definition
    public static var greetingExtension: AppExtensionPoint {
        Name("GreetingUI")
        UserInterface(true)
        Scope(restriction: .none)
    }
}
```

At runtime, the system uses your app’s `.appext` file to obtain its extension point information and match your app to app extensions. Starting in iOS 26, iPadOS 26, macOS 26, tvOS 26, and watchOS 26, Xcode supports the programmatic creation this file from the extension point definitions in your app’s source code. To generate this file programmatically, add a user-defined build setting to your app target in Xcode. Set the build setting name to `EX_ENABLE_EXTENSION_POINT_GENERATION` and configure it with a value of `YES`.

> **Note**: In you already created an `.appext` file for your app, you may continue to use the file you created.

##### Launch an App Extension and Connect to It Using Xpc

In your app’s code, you decide when is the best time to launch an app extension and take advantage of its features. When a particular task requires an app extension, use the [`ExtensionFoundation`](ExtensionFoundation.md) framework to find the extension you want and launch it. As part of the launch process, establish an XPC connection to the app extension and use that connection to send and receive data.

After locating the app extension you want to run, create and configure an [`AppExtensionProcess`](appextensionprocess.md) structure in your app. The configuration object you pass to the initializer contains the app extension’s identity along with code to handle potential issues. The system returns a new instance of the type to your code only after the successfully connecting to the new process. When you have that instance, create an XPC connection and retrieve the remote object to use for communication, as shown in the following code:

```swift
// Create the app extension process and an XPC connection to it.
let appExtProcess = try AppExtensionProcess(configuration: config)
let xpcConnection = try appExtProcess.makeXPCConnection()
            
// Get the proxy object for communicating with the app extension.
proxyObj = xpcConnection.remoteObjectProxyWithErrorHandler { error in
    print("Unable to get remote object: \(error)")
} as? MyRemoteInterface
```

> **Note**: The system connects to an existing process when one is available or launches a new process as needed. After launch, the app extension runs long enough for you to create an XPC connection to it. If you don’t make a connection right away, the system may suspend the app extension, waking it again only when you subsequently try to make an XPC connection to it.

Use the proxy object from your XPC connection to send data to the app extension and receive responses. The proxy object is local to your app, but doesn’t do the actual work associated with its interface. Instead, proxy objects forward requests to the app extension’s process for fulfillment.

For information about how to find the app extensions available for you to run, see [`Discovering app extensions from your app`](discovering-app-extensions-from-your-app.md). For information about how to accept an XPC connection in your app extension code, see [`Building an app extension to support a host app`](building-an-app-extension-to-support-a-host-app.md). For information about how to connect to an app extension with custom UI, see [`Including extension-based UI in your interface`](https://developer.apple.com/documentation/ExtensionKit/including-extension-based-ui-in-your-interface).

##### Unload App Extensions When You Finish with Them

When your app no longer needs an app extension, call the [`invalidate()`](appextensionprocess/invalidate().md) method of the associated [`AppExtensionProcess`](appextensionprocess.md) structure. Invalidating an app extension process severs the current connection to that process, but doesn’t automatically terminate it. If an app extension has multiple active connections, the system keeps the process alive until the last connection closes.

> ❗ **Important**: Keep a strong reference to any [`AppExtensionProcess`](appextensionprocess.md) structures you create.
If you don’t maintain a reference to the structures, the system invalidates connections to those app extensions automatically.

If the app extension’s process terminates unexpectedly, the [`AppExtensionProcess`](appextensionprocess.md) structure runs the `onInterruption` handler you supplied at configuration time. Use that handler to clean up references to proxy objects and the associated XPC connection types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/adding-support-for-app-extensions-to-your-app)*