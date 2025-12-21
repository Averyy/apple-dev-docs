# scaledToFit()

**Framework**: SwiftUI  
**Kind**: method

Scales this view to fit its parent.

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
nonisolated
func scaledToFit() -> some View
```

#### Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect ratio.

#### Discussion

Use `scaledToFit()` to scale this view to fit its parent, while maintaining the view’s aspect ratio as the view scales.

```swift
Circle()
    .fill(Color.pink)
    .scaledToFit()
    .frame(width: 300, height: 150)
    .border(Color(white: 0.75))
```

![A screenshot of pink circle scaled to fit its](https://docs-assets.developer.apple.com/published/beb6f09bb88fe40b033eed2bd645f008/SwiftUI-View-scaledToFit-1%402x.png)

This method is equivalent to calling [`aspectRatio(_:contentMode:)`](view/aspectratio(_:contentmode:).md) with a `nil` aspectRatio and a content mode of [`ContentMode.fit`](contentmode/fit.md).

## See Also

- [func scaledToFill() -> some View](view/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaleEffect(_:anchor:)](view/scaleeffect(_:anchor:).md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaledtofit())*