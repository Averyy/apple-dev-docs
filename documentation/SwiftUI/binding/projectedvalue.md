# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the binding value that returns a binding.

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
var projectedValue: Binding<Value> { get }
```

#### Discussion

Use the projected value to pass a binding value down a view hierarchy. To get the `projectedValue`, prefix the property variable with `$`. For example, in the following code example `PlayerView` projects a binding of the state property `isPlaying` to the `PlayButton` view using `$isPlaying`.

```swift
struct PlayerView: View {
    var episode: Episode
    @State private var isPlaying: Bool = false

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

- [var wrappedValue: Value](binding/wrappedvalue.md)
  The underlying value referenced by the binding variable.
- [subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) -> Binding<Subject>](binding/subscript(dynamicmember:).md)
  Returns a binding to the resulting value of a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/projectedvalue)*