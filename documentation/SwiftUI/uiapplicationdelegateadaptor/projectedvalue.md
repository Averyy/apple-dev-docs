# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the observed object that provides bindings to its properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

#### Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your application delegate:

```swift
class MyAppDelegate: NSObject, UIApplicationDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [`App`](app.md) using the [`UIApplicationDelegateAdaptor`](uiapplicationdelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your app:

```swift
struct MyView: View {
    @EnvironmentObject private var appDelegate: MyAppDelegate

    var body: some View {
        Toggle("Enabled", isOn: $appDelegate.isEnabled)
    }
}
```

## See Also

- [var wrappedValue: DelegateType](uiapplicationdelegateadaptor/wrappedvalue.md)
  The underlying app delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue)*