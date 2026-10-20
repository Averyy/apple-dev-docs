# accessibility

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The kind for accessibility visuals and sorting.

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
static let accessibility: ContentShapeKinds
```

#### Discussion

Setting a content shape with this kind causes the accessibility frame and path of the view’s underlying accessibility element to match the shape without adjusting the hit-testing shape, updating the visual focus ring that assistive apps, such as VoiceOver, draw, as well as how the element is sorted. Updating the accessibility shape is only required if the shape or size used to hit-test significantly diverges from the visual shape of the view.

To control the shape for accessibility and hit-testing, use the `interaction` kind.

## See Also

### Getting shape kinds
- [static let interaction: ContentShapeKinds](./interaction.md)
  The kind for hit-testing and accessibility.
- [static let dragPreview: ContentShapeKinds](./dragpreview.md)
  The kind for drag and drop previews.
- [static let contextMenuPreview: ContentShapeKinds](./contextmenupreview.md)
  The kind for context menu previews.
- [static let focusEffect: ContentShapeKinds](./focuseffect.md)
  The kind for the focus effect.
- [static let hoverEffect: ContentShapeKinds](./hovereffect.md)
  The kind for hover effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentshapekinds/accessibility)*