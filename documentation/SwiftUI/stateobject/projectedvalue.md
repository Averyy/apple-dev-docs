# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the state object that creates bindings to its properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: ObservedObject<ObjectType>.Wrapper { get }
```

#### Discussion

Use the projected value to get a [`Binding`](binding.md) to a property of a state object. To access the projected value, prefix the property name with a dollar sign (`$`). For example, you can get a binding to a model’s `isEnabled` Boolean so that a [`Toggle`](toggle.md) can control the value:

```swift
struct MyView: View {
    @StateObject private var model = DataModel()

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

> ❗ **Important**: A `Binding` created by the projected value must only be read from, or written to by the main actor. Failing to do so may result in undefined behavior, or data loss. When this occurs, SwiftUI will issue a runtime warning. In a future release, a crash will occur instead.

A `Binding` created by the projected value must only be read from, or written to by the main actor. Failing to do so may result in undefined behavior, or data loss. When this occurs, SwiftUI will issue a runtime warning. In a future release, a crash will occur instead.

## See Also

- [var wrappedValue: ObjectType](stateobject/wrappedvalue.md)
  The underlying value referenced by the state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stateobject/projectedvalue)*