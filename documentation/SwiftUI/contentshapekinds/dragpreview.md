# dragPreview

**Framework**: SwiftUI  
**Kind**: property

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

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

#### Discussion

When using this kind, only the preview shape is affected. To control the shape used to hit-test and start the drag preview, use the `interaction` kind.

## See Also

- [static let interaction: ContentShapeKinds](contentshapekinds/interaction.md)
  The kind for hit-testing and accessibility.
- [static let contextMenuPreview: ContentShapeKinds](contentshapekinds/contextmenupreview.md)
  The kind for context menu previews.
- [static let focusEffect: ContentShapeKinds](contentshapekinds/focuseffect.md)
  The kind for the focus effect.
- [static let hoverEffect: ContentShapeKinds](contentshapekinds/hovereffect.md)
  The kind for hover effects.
- [static let accessibility: ContentShapeKinds](contentshapekinds/accessibility.md)
  The kind for accessibility visuals and sorting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentshapekinds/dragpreview)*