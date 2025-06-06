# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value referenced by the state variable.

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

## Mentions

- [Managing user interface state](managing-user-interface-state.md)

#### Discussion

This property provides primary access to the value’s data. However, you don’t typically access `wrappedValue` explicitly. Instead, you gain access to the wrapped value by referring to the property variable that you create with the `@State` attribute.

In the following example, the button’s label depends on the value of `isPlaying` and the button’s action toggles the value of `isPlaying`. Both of these accesses implicitly access the state property’s wrapped value:

```swift
struct PlayButton: View {
    @State private var isPlaying: Bool = false

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

## See Also

- [var projectedValue: Binding<Value>](state/projectedvalue.md)
  A binding to the state value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/state/wrappedvalue)*