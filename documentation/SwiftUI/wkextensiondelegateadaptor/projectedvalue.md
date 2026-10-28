# projectedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A projection of the observed object that provides bindings to its properties.

**Availability**:
- watchOS 7.0+ - Deprecated in 9.2

> **Deprecated**: Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to `ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

## Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your extension delegate:

```swift
class MyExtensionDelegate: NSObject, WKExtensionDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [`App`](../app.md) using the [`WKExtensionDelegateAdaptor`](../wkextensiondelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your extension:

```swift
struct MyView: View {
    @EnvironmentObject private var extensionDelegate: MyExtensionDelegate

    var body: some View {
        Toggle("Enabled", isOn: $extensionDelegate.isEnabled)
    }
}
```

## See Also

### Getting the delegate adaptor
- [var wrappedValue: DelegateType](./wrappedvalue.md)
  The underlying delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/projectedvalue)*