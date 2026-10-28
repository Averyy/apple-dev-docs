# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a WatchKit extension delegate adaptor using a delegate that’s an observable object.

**Availability**:
- watchOS 7.0+ - Deprecated in 9.2

> **Deprecated**: Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to `ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

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

Call this initializer indirectly by creating a property with the [`WKExtensionDelegateAdaptor`](../wkextensiondelegateadaptor.md) property wrapper from inside your [`App`](../app.md) declaration:

```swift
@main
struct MyApp: App {
    @WKExtensionDelegateAdaptor private var extensionDelegate: MyExtensionDelegate

    var body: some Scene { ... }
}
```

SwiftUI initializes the delegate and manages its lifetime, calling it as needed to handle extension delegate callbacks.

SwiftUI invokes this method when your extension delegate conforms to the [`ObservableObject`](../../Combine/observableobject.md) protocol. In this case, SwiftUI automatically places the delegate in the [`Environment`](../environment.md). You can access such a delegate from any scene or view in your app using the [`EnvironmentObject`](../environmentobject.md) property wrapper:

```swift
@EnvironmentObject private var appDelegate: MyAppDelegate
```

If your delegate isn’t an observable object, SwiftUI invokes the [`init(_:)`](./init%28_%29-2556.md) initializer rather than this one, and doesn’t put the delegate instance in the environment.

## Parameters

- `delegateType`: The type of extension delegate that you define in your app, which conforms to the [`WKExtensionDelegate`](../../WatchKit/wkextensiondelegate.md) and [`ObservableObject`](../../Combine/observableobject.md) protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/init(_:)-2btqx)*