# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value referenced by the binding variable.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var wrappedValue: Value { get nonmutating set }
```

#### Discussion

This property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you use the property variable created with the [`Binding`](binding.md) attribute. In the following code example, the binding variable `isPlaying` returns the value of `wrappedValue`:

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

When a mutable binding value changes, the new value is immediately available. However, updates to a view displaying the value happens asynchronously, so the view may not show the change immediately.

## See Also

- [var projectedValue: Binding<Value>](binding/projectedvalue.md)
  A projection of the binding value that returns a binding.
- [subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) -> Binding<Subject>](binding/subscript(dynamicmember:).md)
  Returns a binding to the resulting value of a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/wrappedvalue)*