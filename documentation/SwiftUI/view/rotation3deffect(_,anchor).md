# rotation3DEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Rotates the view’s content by the specified 3D rotation value.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func rotation3DEffect(_ rotation: Rotation3D, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```swift
Model3D(named: "robot")
    .rotation3DEffect(Rotation3D(angle: .degrees(45), axis: .y))
```

During an animation, this modifier uses spherical linear interpolation, which produces more natural animations, but doesn’t support rotations over 360 degrees. To specify angles over 360 degrees, consider using `View/rotation3DEffect(_:axis:anchor:)-4enag`.

## Parameters

- `rotation`: A rotation to apply to the view’s content.
- `anchor`: The unit point within the view about which to perform the rotation. The default value is [`center`](../unitpoint3d/center.md).

## See Also

### Scaling, rotating, or transforming a view
- [func scaledToFill() -> some View](./scaledtofill%28%29.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](./scaledtofit%28%29.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](./scaleeffect%28_,anchor%29.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](./scaleeffect%28x,y,anchor%29.md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](./scaleeffect%28x,y,z,anchor%29.md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func aspectRatio(_:contentMode:)](./aspectratio%28_,contentmode%29.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](./rotationeffect%28_,anchor%29.md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./rotation3deffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./perspectiverotationeffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(_:axis:anchor:)](./rotation3deffect%28_,axis,anchor%29.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func transformEffect(CGAffineTransform) -> some View](./transformeffect%28_%29.md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](./transform3deffect%28_%29.md)
  Applies a 3D transformation to this view’s rendered output.
- [func projectionEffect(ProjectionTransform) -> some View](./projectioneffect%28_%29.md)
  Applies a projection transformation to this view’s rendered output.
- [struct ProjectionTransform](../projectiontransform.md)
  A 3x3 matrix that transforms points in a plane.
- [enum ContentMode](../contentmode.md)
  Constants that define how a view’s content fills the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/rotation3deffect(_:anchor:))*