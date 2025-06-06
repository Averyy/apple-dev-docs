# NSRunningApplication

**Framework**: AppKit  
**Kind**: class

An object that can manipulate and provide information for a single instance of an app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class NSRunningApplication
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Overview

Some properties of an app are fixed, such as the bundle identifier. Other properties may vary over time, such as whether the app is hidden. Properties that vary can be observed with key-value observing, in which case the description comment for the method notes this capability.

Properties that vary over time are inherently race-prone. For example, a hidden app may unhide itself at any time. To ameliorate this, properties persist until the next turn of the main run loop in a common mode. For example, if you repeatedly poll an unhidden app for its hidden property without allowing the run loop to run, it will continue to return [`false`](https://developer.apple.com/documentation/swift/false), even if the app hides, until the next turn of the run loop.

[`NSRunningApplication`](nsrunningapplication.md) is thread safe, in that its properties are returned atomically. However, it is still subject to the main run loop policy described above. If you access an instance of [`NSRunningApplication`](nsrunningapplication.md) from a background thread, be aware that its time-varying properties may change from under you as the main run loop runs (or not).

An [`NSRunningApplication`](nsrunningapplication.md) instance remains valid after the app exits. However, most properties lose their significance, and some properties may not be available on a terminated application.

To access the list of all running apps, use the  [`runningApplications`](nsworkspace/runningapplications.md) method in [`NSWorkspace`](nsworkspace.md).

## Topics

### Getting running application instances
- [convenience init?(processIdentifier: pid_t)](nsrunningapplication/init(processidentifier:).md)
  Returns the running application with the given process identifier, or nil if no application has that pid.
- [class func runningApplications(withBundleIdentifier: String) -> [NSRunningApplication]](nsrunningapplication/runningapplications(withbundleidentifier:).md)
  Returns an array of currently running applications with the specified bundle identifier.
- [class var current: NSRunningApplication](nsrunningapplication/current.md)
  Returns an `NSRunningApplication` representing this application.
### Activating applications
- [func activate(options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(options:).md)
  Attempts to activate the application using the specified options.
- [func activate(from: NSRunningApplication, options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(from:options:).md)
  Attempts to activate the application using the specified options.
- [var isActive: Bool](nsrunningapplication/isactive.md)
  Indicates whether the application is currently frontmost.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).
- [var activationPolicy: NSApplication.ActivationPolicy](nsrunningapplication/activationpolicy.md)
  Indicates the activation policy of the application.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.
### Hiding and unhiding applications
- [func hide() -> Bool](nsrunningapplication/hide.md)
  Attempts to hide or the application.
- [func unhide() -> Bool](nsrunningapplication/unhide.md)
  Attempts to unhide or the application.
- [var isHidden: Bool](nsrunningapplication/ishidden.md)
  Indicates whether the application is currently hidden.
### Application information
- [var localizedName: String?](nsrunningapplication/localizedname.md)
  Indicates the localized name of the application.
- [var icon: NSImage?](nsrunningapplication/icon.md)
  Returns the icon for the receiver’s application.
- [var bundleIdentifier: String?](nsrunningapplication/bundleidentifier.md)
  Indicates the `CFBundleIdentifier` of the application.
- [var bundleURL: URL?](nsrunningapplication/bundleurl.md)
  Indicates the URL to the application’s bundle.
- [var executableArchitecture: Int](nsrunningapplication/executablearchitecture.md)
  Indicates the executing processor architecture for the application.
- [var executableURL: URL?](nsrunningapplication/executableurl.md)
  Indicates the URL to the application’s executable.
- [var launchDate: Date?](nsrunningapplication/launchdate.md)
  Indicates the date when the application was launched.
- [var isFinishedLaunching: Bool](nsrunningapplication/isfinishedlaunching.md)
  Indicates whether the receiver’s process has finished launching,
- [var processIdentifier: pid_t](nsrunningapplication/processidentifier.md)
  Indicates the process identifier (pid) of the application.
- [var ownsMenuBar: Bool](nsrunningapplication/ownsmenubar.md)
  Returns whether the application owns the current menu bar.
### Terminating applications
- [func forceTerminate() -> Bool](nsrunningapplication/forceterminate.md)
  Attempts to force the receiver to quit.
- [func terminate() -> Bool](nsrunningapplication/terminate.md)
  Attempts to quit the receiver normally.
- [var isTerminated: Bool](nsrunningapplication/isterminated.md)
  Indicates that the receiver’s application has terminated.
- [class func terminateAutomaticallyTerminableApplications()](nsrunningapplication/terminateautomaticallyterminableapplications.md)
  Terminates invisibly running applications as if triggered by system memory pressure.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSApplication](nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [protocol NSApplicationDelegate](nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.
- [func NSApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32](nsapplicationmain(_:_:).md)
  Called by the main function to create and run the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication)*