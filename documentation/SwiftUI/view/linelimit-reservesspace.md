# lineLimit(_:reservesSpace:)

**Framework**: SwiftUI  
**Kind**: method

Sets a limit for the number of lines text can occupy in this view.

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
func lineLimit(_ limit: Int, reservesSpace: Bool) -> some View
```

#### Discussion

Use this modifier to specify a limit to the lines that a [`Text`](text.md) or a vertical [`TextField`](textfield.md) may occupy. If passed a value of true for the `reservesSpace` parameter, and the text of such views occupies less space than the provided limit, that view expands to occupy the minimum number of lines. When the text occupies more space than the provided limit, a [`Text`](text.md) view truncates its content while a [`TextField`](textfield.md) becomes scrollable.

```swift
GroupBox {
    Text("Title")
        .font(.headline)
        .lineLimit(2, reservesSpace: true)
    Text("Subtitle")
        .font(.subheadline)
        .lineLimit(4, reservesSpace: true)
}
```

## Parameters

- `limit`: The line limit.
- `reservesSpace`: Whether text reserves space so that   it always occupies the height required to display the specified   number of lines.

## See Also

- [func lineLimit(_:)](view/linelimit(_:).md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [var lineLimit: Int?](environmentvalues/linelimit.md)
  The maximum number of lines that text can occupy in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/linelimit(_:reservesspace:))*