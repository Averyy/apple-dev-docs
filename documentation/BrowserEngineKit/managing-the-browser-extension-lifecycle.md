# Managing the browser extension life cycle

**Framework**: BrowserEngineKit

Coordinate helper processes to efficiently support your browser app.

#### Overview

When your browser app uses an alternative browser engine, it relies on helper processes to access operating-system resources and work with untrusted resources, following the security principle of least privilege. Use the [`BrowserEngineKit`](BrowserEngineKit.md) framework to manage these processes, and notify the operating system of the status of each process as it supports your browser app.

##### Launch Browser Extensions

Your browser app acts as the “host” for each of the extensions that support your browser engine. You need to include the code to launch each extension in your browser app; one extension can’t load another extension.

To launch an extension, your browser app creates and initializes an instance of the structure that represents the running extension process. Pass an  to the initializer, to execute cleanup code if the operating system interrupts the extension process or the extension crashes. For example, to launch a web content extension:

```swift
let contentProcess = WebContentProcess() {
  // Handle the web content extension getting interrupted.
}
```

To launch the GPU extension, create a [`RenderingProcess`](renderingprocess.md) instead of a [`WebContentProcess`](webcontentprocess.md). To launch the networking extension, create a [`NetworkingProcess`](networkingprocess.md) instead.

##### Communicate Between Your Browser App and Its Extensions

Use the [`WebContentProcess`](webcontentprocess.md), [`RenderingProcess`](renderingprocess.md), and [`NetworkingProcess`](networkingprocess.md) objects to create inter-process communication (IPC) channels between your host app and the extensions.

For more information, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

##### Put the Content Extension in a Restricted Sandbox

The operating system creates a temporary sandbox when it starts your content extension process, which gives the extension access to resources it uses during initialization. For more information: see [`Limiting resource access in web content extensions`](limiting-resource-access-in-content-extensions.md).

##### Grant and Invalidate Extension Capabilities

As your extensions participate in your browser app’s workflow, grant them capabilities that tell the operating system what your browser is using the extensions for. Capabilities act as assertions to the operating system that it needs to schedule the extension to support particular tasks, for example preparing media content to display in a tab that’s in the foreground on the person’s screen.

You identify the capability to grant to the extension by selecting the appropriate value from the [`ProcessCapability`](processcapability.md) enumeration. In your browser app, pass the capability  to the extension process’s `grantCapability()` method to receive a  object of type [`ProcessCapability.Grant`](processcapability/grant.md), indicating that the operating system granted the capability to your extension. When you finish the task that requires the capability, call [`invalidate()`](processcapability/grant/invalidate().md) on the grant object to relinquish the capability.

For example, to request and use the [`ProcessCapability.foreground`](processcapability/foreground.md) capability for the networking process:

```swift
if let grant = try? networkingProcess.grant(.foreground) {
  // Use XPC to send messages to the networking extension while it has the capability.
  grant.invalidate()
} else {
  // The operating system didn't grant the capability to the extension.
}
```

##### Stop Extension Processes

When you no longer need an extension process, call its `invalidate()` method to indicate to the operating system that it can stop the process. Once you have invalidated a process, it’s an error to call other methods on the process object.

## See Also

- [Using XPC to communicate with browser extensions](using-xpc-to-communicate-with-browser-extensions.md)
  Build interprocess communication between your host app and extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/managing-the-browser-extension-lifecycle)*