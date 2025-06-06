# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a WatchKit extension delegate adaptor using an observable delegate.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

#### Discussion

Call this initializer indirectly by creating a property with the [`WKExtensionDelegateAdaptor`](wkextensiondelegateadaptor.md) property wrapper from inside your [`App`](app.md) declaration:

```swift
@main
struct MyApp: App {
    @WKExtensionDelegateAdaptor private var extensionDelegate: MyExtensionDelegate

    var body: some Scene { ... }
}
```

SwiftUI initializes the delegate and manages its lifetime, calling it as needed to handle extension delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol. In this case, SwiftUI automatically places the delegate in the [`Environment`](environment.md). You can access such a delegate from any scene or view in your app using the [`Environment`](environment.md) property wrapper:

```swift
@Environment(MyAppDelegate.self) private var appDelegate
```

If your delegate isn’t observable, SwiftUI invokes the [`init(_:)`](wkextensiondelegateadaptor/init(_:)-2556.md) initializer rather than this one, and doesn’t put the delegate instance in the environment.

## Parameters

- `delegateType`: The type of extension delegate that you   define in your app, which conforms to the     and     protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/init(_:))*