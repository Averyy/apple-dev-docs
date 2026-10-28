# dragPreview

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The kind for drag and drop previews.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let dragPreview: ContentShapeKinds
```

## Mentions

- [Making a view into a drag source](../making-a-view-into-a-drag-source.md)

## Discussion

When using this kind, only the preview shape is affected. To control the shape used to hit-test and start the drag preview, use the `interaction` kind.

## See Also

### Getting shape kinds
- [static let interaction: ContentShapeKinds](./interaction.md)
  The kind for hit-testing and accessibility.
- [static let contextMenuPreview: ContentShapeKinds](./contextmenupreview.md)
  The kind for context menu previews.
- [static let focusEffect: ContentShapeKinds](./focuseffect.md)
  The kind for the focus effect.
- [static let hoverEffect: ContentShapeKinds](./hovereffect.md)
  The kind for hover effects.
- [static let accessibility: ContentShapeKinds](./accessibility.md)
  The kind for accessibility visuals and sorting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentshapekinds/dragpreview)*