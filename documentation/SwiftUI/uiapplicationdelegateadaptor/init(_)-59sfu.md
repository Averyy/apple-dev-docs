# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a UIKit app delegate adaptor.

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

SwiftUI initializes the delegate and manages its lifetime, calling upon it to handle application delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the [`Environment`](../environment.md), make sure the delegate class also conforms to the [`ObservableObject`](../../Combine/observableobject.md) protocol. That causes SwiftUI to invoke the [`init(_:)`](./init%28_%29-8vsx1.md) initializer rather than this one.

## Parameters

- `delegateType`: The type of application delegate that you define in your app, which conforms to the [`UIApplicationDelegate`](../../UIKit/uiapplicationdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/init(_:)-59sfu)*