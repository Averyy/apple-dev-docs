# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the observed object that provides bindings to its properties.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

#### Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your application delegate:

```swift
class MyAppDelegate: NSObject, NSApplicationDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [`App`](app.md) using the [`NSApplicationDelegateAdaptor`](nsapplicationdelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your app:

```swift
struct MyView: View {
    @EnvironmentObject private var appDelegate: MyAppDelegate

    var body: some View {
        Toggle("Enabled", isOn: $appDelegate.isEnabled)
    }
}
```

## See Also

- [var wrappedValue: DelegateType](nsapplicationdelegateadaptor/wrappedvalue.md)
  The underlying delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor/projectedvalue)*