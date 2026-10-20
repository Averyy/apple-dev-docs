# ContentMode

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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

- [Fitting images into available space](./fitting-images-into-available-space.md)

## Topics

### Getting content modes
- [ContentMode.fill](./contentmode/fill.md)
  An option that resizes the content so it occupies all available space, both vertically and horizontally.
- [ContentMode.fit](./contentmode/fit.md)
  An option that resizes the content so it’s all within the available space, both vertically and horizontally.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scaling, rotating, or transforming a view
- [func scaledToFill() -> some View](./view/scaledtofill%28%29.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](./view/scaledtofit%28%29.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](./view/scaleeffect%28_,anchor%29.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](./view/scaleeffect%28x,y,anchor%29.md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](./view/scaleeffect%28x,y,z,anchor%29.md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func aspectRatio(_:contentMode:)](./view/aspectratio%28_,contentmode%29.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](./view/rotationeffect%28_,anchor%29.md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./view/rotation3deffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./view/perspectiverotationeffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](./view/rotation3deffect%28_,anchor%29.md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](./view/rotation3deffect%28_,axis,anchor%29.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func transformEffect(CGAffineTransform) -> some View](./view/transformeffect%28_%29.md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](./view/transform3deffect%28_%29.md)
  Applies a 3D transformation to this view’s rendered output.
- [func projectionEffect(ProjectionTransform) -> some View](./view/projectioneffect%28_%29.md)
  Applies a projection transformation to this view’s rendered output.
- [struct ProjectionTransform](./projectiontransform.md)
  A 3x3 matrix that transforms points in a plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmode)*