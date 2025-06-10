# ContentMode

**Framework**: SwiftUI  
**Kind**: enum

Constants that define how a view’s content fills the available space.

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
@frozen
enum ContentMode
```

## Mentions

- [Fitting images into available space](fitting-images-into-available-space.md)

## Topics

### Getting content modes
- [ContentMode.fill](contentmode/fill.md)
  An option that resizes the content so it occupies all available space, both vertically and horizontally.
- [ContentMode.fit](contentmode/fit.md)
  An option that resizes the content so it’s all within the available space, both vertically and horizontally.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scaledToFill() -> some View](view/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](view/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](view/scaleeffect(_:anchor:).md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](view/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](view/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func aspectRatio(_:contentMode:)](view/aspectratio(_:contentmode:).md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](view/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](view/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](view/rotation3deffect(_:axis:anchor:).md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func transformEffect(CGAffineTransform) -> some View](view/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](view/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
- [func projectionEffect(ProjectionTransform) -> some View](view/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [struct ProjectionTransform](projectiontransform.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmode)*