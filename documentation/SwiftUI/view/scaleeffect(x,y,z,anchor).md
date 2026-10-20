# scaleEffect(x:y:z:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, z: CGFloat = 1.0, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view that scales this view by `x`,`y`, and `z`.

#### Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `x`: The horizontal scale factor for this view.
- `y`: The vertical scale factor for this view.
- `z`: The depth scale factor for this view.
- `anchor`: The anchor point about which to scale the view. Defaults to center.

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
- [func aspectRatio(_:contentMode:)](./aspectratio%28_,contentmode%29.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](./rotationeffect%28_,anchor%29.md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./rotation3deffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./perspectiverotationeffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](./rotation3deffect%28_,anchor%29.md)
  Rotates the view’s content by the specified 3D rotation value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaleeffect(x:y:z:anchor:))*