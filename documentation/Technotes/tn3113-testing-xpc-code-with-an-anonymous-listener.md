# TN3113: Testing and debugging XPC code with an anonymous listener

**Framework**: Technotes

Use an anonymous XPC listener to simplify your XPC testing and debugging.

#### Overview

Testing and debugging XPC code is tricky because there are two processes involved.  Imagine you have an app with an embedded XPC service.  To debug this you have to run two instances of the debugger, one connected to the app and another to the service, and then switch between them.  This works, but it’s quite inconvenient.  Fortunately there is a better way, a technique that allows you to test and debug all your XPC code in a single process.

> ❗ **Important**: This technique does not help with all XPC testing and debugging scenarios.  For example, if you’re developing a `launchd` daemon that performs privileged operations on behalf of your app, you can’t use this technique to debug your privileged code because it’s not running in a privileged process.  However, even in situations like that, this technique is useful when debugging your XPC-specific code.  For example, you might use it to create a unit test for your [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) implementation.

This technique does not help with all XPC testing and debugging scenarios.  For example, if you’re developing a `launchd` daemon that performs privileged operations on behalf of your app, you can’t use this technique to debug your privileged code because it’s not running in a privileged process.  However, even in situations like that, this technique is useful when debugging your XPC-specific code.  For example, you might use it to create a unit test for your [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) implementation.

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

While this example uses the Foundation [`XPC`](https://developer.apple.com/documentation/Foundation/xpc) API, the same technique works for the low-level C [`XPC`](https://developer.apple.com/documentation/XPC) API.

Change its initialiser to look like this:

```swift
init(listener: NSXPCListener = .service()) {
    self.listener = listener
}
```

This uses the XPC service’s listener by default, but allows you to override that by passing in a value to the `listener` parameter.

Now, in your test program, call [`anonymousListener`](https://developer.apple.com/documentation/foundation/nsxpclistener/1412648-anonymouslistener) to create a anonymous listener and pass that to your listener abstraction:

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

Finally, in your test program, use `init(listenerEndpoint:)` to create a connection to your anonymous listener:

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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3113-testing-xpc-code-with-an-anonymous-listener)*