# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a UIKit app delegate adaptor using a delegate that’s an observable object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to `ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

**Other overloads**:

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

## Discussion

Call this initializer indirectly by creating a property with the [`UIApplicationDelegateAdaptor`](../uiapplicationdelegateadaptor.md) property wrapper from inside your [`App`](../app.md) declaration:

```swift
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate

    var body: some Scene { ... }
}
```

SwiftUI initializes the delegate and manages its lifetime, calling it as needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the [`ObservableObject`](../../Combine/observableobject.md) protocol. In this case, SwiftUI automatically places the delegate in the [`Environment`](../environment.md). You can access such a delegate from any scene or view in your app using the [`EnvironmentObject`](../environmentobject.md) property wrapper:

```swift
@EnvironmentObject private var appDelegate: MyAppDelegate
```

If your delegate isn’t an observable object, SwiftUI invokes the [`init(_:)`](./init%28_%29-59sfu.md) initializer rather than this one, and doesn’t put the delegate instance in the environment.

## Parameters

- `delegateType`: The type of application delegate that you define in your app, which conforms to the [`UIApplicationDelegate`](../../UIKit/uiapplicationdelegate.md) and [`ObservableObject`](../../Combine/observableobject.md) protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/init(_:)-8vsx1)*