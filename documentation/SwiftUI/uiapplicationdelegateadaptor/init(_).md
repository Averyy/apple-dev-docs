# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a UIKit app delegate adaptor using an observable delegate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to `Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

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

SwiftUI invokes this method when your app delegate conforms to the [`Observable`](../../Observation/observable.md) protocol. In this case, SwiftUI automatically places the delegate in the [`Environment`](../environment.md). You can access such a delegate from any scene or view in your app using the [`Environment`](../environment.md) property wrapper:

```swift
@Environment(MyAppDelegate.self) private var appDelegate
```

If your delegate isn’t observable, SwiftUI invokes the [`init(_:)`](./init%28_%29-59sfu.md) initializer rather than this one, and doesn’t put the delegate instance in the environment.

## Parameters

- `delegateType`: The type of application delegate that you define in your app, which conforms to the [`UIApplicationDelegate`](../../UIKit/uiapplicationdelegate.md) and [`Observable`](../../Observation/observable.md) protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/init(_:))*