# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value referenced by the state variable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var wrappedValue: Value { get nonmutating set }
```

#### Discussion

This property provides primary access to the value’s data. However, you don’t typically access `wrappedValue` explicitly. Instead, you gain access to the wrapped value by referring to the property variable that you create with the `@LazyState` attribute.

In the following example, the button’s label depends on the value of `isPlaying` and the button’s action toggles the value of `isPlaying`. Both of these accesses implicitly access the state property’s wrapped value:

```swift
struct PlayButton: View {
    @LazyState private var isPlaying: Bool = false

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

## See Also

- [var projectedValue: Binding<Value>](lazystate/projectedvalue.md)
  A binding to the state value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazystate/wrappedvalue)*