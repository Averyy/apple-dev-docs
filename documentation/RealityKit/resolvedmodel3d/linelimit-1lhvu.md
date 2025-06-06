# lineLimit(_:)

**Framework**: RealityKit  
**Kind**: method

Sets to a partial range the number of lines that text can occupy in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func lineLimit(_ limit: PartialRangeFrom<Int>) -> some View
```

#### Discussion

Use this modifier to specify a partial range of lines that a `Text` view or a vertical `TextField` can occupy. When the text of such views occupies less space than the provided limit, that view expands to occupy the minimum number of lines.

```None
Form {
    TextField("Title", text: $model.title)
    TextField("Notes", text: $model.notes, axis: .vertical)
        .lineLimit(3...)
}
```

## Parameters

- `limit`: The line limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/linelimit(_:)-1lhvu)*