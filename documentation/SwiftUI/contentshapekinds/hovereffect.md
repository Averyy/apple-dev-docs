# hoverEffect

**Framework**: SwiftUI  
**Kind**: property

The kind for hover effects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
static let hoverEffect: ContentShapeKinds
```

#### Discussion

When using this kind, only the preview shape is affected. To control the shape used to hit-test and start the effect, use the `interaction` kind.

On tvOS, this is used to define the shape of any hover effect applied to focusable and hoverable controls, for example button border or clipping shapes.

This kind does not affect the `onHover` modifier.

## See Also

- [static let interaction: ContentShapeKinds](contentshapekinds/interaction.md)
  The kind for hit-testing and accessibility.
- [static let dragPreview: ContentShapeKinds](contentshapekinds/dragpreview.md)
  The kind for drag and drop previews.
- [static let contextMenuPreview: ContentShapeKinds](contentshapekinds/contextmenupreview.md)
  The kind for context menu previews.
- [static let focusEffect: ContentShapeKinds](contentshapekinds/focuseffect.md)
  The kind for the focus effect.
- [static let accessibility: ContentShapeKinds](contentshapekinds/accessibility.md)
  The kind for accessibility visuals and sorting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentshapekinds/hovereffect)*