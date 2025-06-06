# lineLimit(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets to a closed range the number of lines that text can occupy in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func lineLimit(_ limit: ClosedRange<Int>) -> some View
```

#### Discussion

Use this modifier to specify a closed range of lines that a [`Text`](text.md) view or a vertical [`TextField`](textfield.md) can occupy. When the text of such views occupies more space than the provided limit, a [`Text`](text.md) view truncates its content while a [`TextField`](textfield.md) becomes scrollable.

```swift
Form {
    TextField("Title", text: $model.title)
    TextField("Notes", text: $model.notes, axis: .vertical)
        .lineLimit(1...3)
}
```

## Parameters

- `limit`: The line limit.

## See Also

- [func lineLimit(Int, reservesSpace: Bool) -> some View](view/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [var lineLimit: Int?](environmentvalues/linelimit.md)
  The maximum number of lines that text can occupy in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/linelimit(_:))*