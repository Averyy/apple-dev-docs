# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A binding to the state value.

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
var projectedValue: Binding<Value> { get }
```

#### Discussion

Use the projected value to get a [`Binding`](binding.md) to the stored value. The binding provides a two-way connection to the stored value. To access the `projectedValue`, prefix the property variable with a dollar sign (`$`).

In the following example, `PlayerView` projects a binding of the state property `isPlaying` to the `PlayButton` view using `$isPlaying`. That enables the play button to both read and write the value:

```swift
struct PlayerView: View {
    var episode: Episode
    @LazyState private var isPlaying: Bool = false

    var body: some View {
        VStack {
            Text(episode.title)
                .foregroundStyle(isPlaying ? .primary : .secondary)
            PlayButton(isPlaying: $isPlaying)
        }
    }
}
```

## See Also

- [var wrappedValue: Value](lazystate/wrappedvalue.md)
  The underlying value referenced by the state variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazystate/projectedvalue)*