# NSApplicationDelegateAdaptor

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that you use to create an AppKit app delegate.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency @propertyWrapper struct NSApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : NSApplicationDelegate
```

## Mentions

- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)

#### Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle, define a type that conforms to the [`NSApplicationDelegate`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate) protocol, and implement the delegate methods that you need. For example, you can implement the [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:didRegisterForRemoteNotificationsWithDeviceToken:)) method to handle remote notification registration:

```swift
class MyAppDelegate: NSObject, NSApplicationDelegate, ObservableObject {
    func application(
        _ application: NSApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        // Record the device token.
    }
}
```

Then use the `NSApplicationDelegateAdaptor` property wrapper inside your [`App`](app.md) declaration to tell SwiftUI about the delegate type:

```swift
@main
struct MyApp: App {
    @NSApplicationDelegateAdaptor private var appDelegate: MyAppDelegate

    var body: some Scene { ... }
}
```

SwiftUI instantiates the delegate and calls the delegate’s methods in response to life cycle events. Define the delegate adaptor only in your [`App`](app.md) declaration, and only once for a given app. If you declare it more than once, SwiftUI generates a runtime error.

If your app delegate conforms to the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol, as in the example above, then SwiftUI puts the delegate it creates into the [`Environment`](environment.md). You can access the delegate from any scene or view in your app using the [`EnvironmentObject`](environmentobject.md) property wrapper:

```swift
@EnvironmentObject private var appDelegate: MyAppDelegate
```

This enables you to use the dollar sign (`$`) prefix to get a binding to published properties that you declare in the delegate. For more information, see [`projectedValue`](nsapplicationdelegateadaptor/projectedvalue.md).

> ❗ **Important**: Manage an app’s life cycle events without using an app delegate whenever possible. For example, prefer to handle changes in [`ScenePhase`](scenephase.md) instead of relying on delegate callbacks, like [`applicationDidFinishLaunching(_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationDidFinishLaunching(_:)).

## Topics

### Creating a delegate adaptor
- [init(_:)](nsapplicationdelegateadaptor/init(_:).md)
  Creates an AppKit app delegate adaptor using an observable delegate.
### Getting the delegate adaptor
- [var projectedValue: ObservedObject<DelegateType>.Wrapper](nsapplicationdelegateadaptor/projectedvalue.md)
  A projection of the observed object that provides bindings to its properties.
- [var wrappedValue: DelegateType](nsapplicationdelegateadaptor/wrappedvalue.md)
  The underlying delegate.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor)*