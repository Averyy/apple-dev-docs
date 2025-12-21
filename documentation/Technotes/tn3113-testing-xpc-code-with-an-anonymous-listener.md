# TN3113: Testing and debugging XPC code with an anonymous listener

**Framework**: Technotes

Use an anonymous XPC listener to simplify your XPC testing and debugging.

#### Overview

Testing and debugging XPC code is tricky because there are two processes involved.  Imagine you have an app with an embedded XPC service.  To debug this you have to run two instances of the debugger, one connected to the app and another to the service, and then switch between them.  This works, but it’s quite inconvenient.  Fortunately there is a better way, a technique that allows you to test and debug all your XPC code in a single process.

> ❗ **Important**: This technique does not help with all XPC testing and debugging scenarios.  For example, if you’re developing a `launchd` daemon that performs privileged operations on behalf of your app, you can’t use this technique to debug your privileged code because it’s not running in a privileged process.  However, even in situations like that, this technique is useful when debugging your XPC-specific code.  For example, you might use it to create a unit test for your [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) implementation.

This technique involves two key concepts:

- Put your XPC listener and XPC client code in the same test program.  The specifics of this program are up to you: It might be a simple test app that you create specifically for this purpose, or it might be an Xcode unit test bundle, or it might be some other kind of program.
- Use an anonymous XPC listener to connect your XPC listener and client code.

Imagine you’re building an app with an embedded XPC service.  You have a `MyListener` class that manages your XPC listener within the XPC service, and a `MyConnection` class that manages the connection on the app side of things.  Add both of those classes, and all their support code, to your test program.  Then change `MyListener` to accept an `NSXPCListener` instance.  For example, your `MyListener` class might look like this:

```swift
class MyListener {

    init() {
        self.listener = NSXPCListener.service()
    }

    let listener: NSXPCListener
    
    … more code …
}
```

> **Note**: While this example uses the Foundation [`XPC`](https://developer.apple.com/documentation/Foundation/xpc) API, the same technique works for the low-level C [`XPC`](https://developer.apple.com/documentation/XPC) API.

Change its initialiser to look like this:

```swift
init(listener: NSXPCListener = .service()) {
    self.listener = listener
}
```

This uses the XPC service’s listener by default, but allows you to override that by passing in a value to the `listener` parameter.

Now, in your test program, call [`anonymous()`](https://developer.apple.com/documentation/Foundation/NSXPCListener/anonymous()) to create a anonymous listener and pass that to your listener abstraction:

```swift
let myListener = MyListener(listener: .anonymous())
```

On the client side, your `MyConnection` class might look like this:

```swift
class MyConnection {

    init() {
        self.connection = NSXPCConnection(serviceName: "com.example.MyService")
    }

    let connection: NSXPCConnection
}
```

Change the initialiser to look like this:

```swift
init(connection: NSXPCConnection = .init(serviceName: "com.example.MyService")) {
    self.connection = connection
}
```

This sets up a connection to the XPC service’s listener by default, but allows you to override that by passing in a value to the `connection` parameter.

Finally, in your test program, use [`init(listenerEndpoint:)`](https://developer.apple.com/documentation/Foundation/NSXPCConnection/init(listenerEndpoint:)) to create a connection to your anonymous listener:

```swift
let connection = NSXPCConnection(listenerEndpoint: myListener.listener.endpoint)
let myConnection = MyConnection(connection: connection)
```

You now have an XPC connection between your client code and your listener, with all the code running in the same test program.  This makes it much easier to debug your XPC code.  And the same technique is perfect for unit tests.

#### Revision History

-  Added syntax highlighting to the code listings (r. 89366505).
-  Republished as TN3113.  Expanded the introduction to clarify the overall concept.  Made other minor editorial changes.
-  First published as ”Testing and Debugging XPC Code With an Anonymous Listener” on Apple Developer Forums.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3113-testing-xpc-code-with-an-anonymous-listener)*