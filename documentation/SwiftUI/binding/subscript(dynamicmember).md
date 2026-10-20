# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a binding to the resulting value of a given key path.

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
subscript<Subject>(dynamicMember keyPath: WritableKeyPath<Value, Subject>) -> Binding<Subject> { get }
```

#### Return Value

A new binding.

#### Overview

Use dynamic member lookup to project a property of the binding’s wrapped value from a key path into a new binding. The returned value is read from, and written to, the original binding. This can be useful when a view accepts a binding for a type that only matches a property of a value from an existing binding.

For example, the `PlayerView` controls the current position for an episode using a `Slider`, and whether the episode is a favorite using a `Toggle`. The view projects the `currentPosition` and `isFavorite` properties of `Episode` into bindings that each of these views accept using dynamic member lookup.

```swift
struct Episode {
    var title: LocalizedStringKey
    var duration: TimeInterval
    var currentPosition: TimeInterval
    var isFavorite: Bool
}

struct PlayerView: View {
    @Binding var episode: Episode

    var body: some View {
        Text(episode.title)
        Toggle("Favorite", isOn: $episode.isFavorite)
        Slider(
            value: $episode.currentPosition,
            in: 0...episode.duration
        )
    }
}
```

## Parameters

- `keyPath`: A key path to a specific resulting value.

## See Also

- [var wrappedValue: Value](binding/wrappedvalue.md)
  The underlying value referenced by the binding variable.
- [var projectedValue: Binding<Value>](binding/projectedvalue.md)
  A projection of the binding value that returns a binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/subscript(dynamicmember:))*