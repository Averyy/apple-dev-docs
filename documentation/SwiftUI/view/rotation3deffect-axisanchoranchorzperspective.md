# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

**Framework**: SwiftUI  
**Kind**: method

Renders a view’s content as if it’s rotated in three dimensions around the specified axis.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+ - Deprecated
- watchOS 6.0+

## Declaration

```swift
nonisolated
func rotation3DEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint = .center, anchorZ: CGFloat = 0, perspective: CGFloat = 1) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

Use this method to create the effect of rotating a view in three dimensions around a specified axis of rotation. The modifier projects the rotated content onto the original view’s plane. Use the `perspective` value to control the renderer’s vanishing point. The following example creates the appearance of rotating text 45˚ about the y-axis:

```swift
Text("Rotation by passing an angle in degrees")
    .rotation3DEffect(
        .degrees(45),
        axis: (x: 0.0, y: 1.0, z: 0.0),
        anchor: .center,
        anchorZ: 0,
        perspective: 1)
    .border(Color.gray)
```

![A screenshot of text in a grey box. The text says Rotation by passing an angle in degrees. The text is rendered in a way that makes it appear farther from the viewer on the right side and closer on the left, as if the text is angled to face someone sitting on the viewer’s right.](https://docs-assets.developer.apple.com/published/26dcde23639ed248bfc573a1a0986072/SwiftUI-View-rotation3DEffect%402x.png)

> ❗ **Important**: In visionOS, create this effect with [`perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)`](view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md) instead. To truly rotate a view in three dimensions, use a 3D rotation modifier without a perspective input like [`rotation3DEffect(_:axis:anchor:)`](view/rotation3deffect(_:axis:anchor:).md).

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation, specified as a tuple with named   elements for each of the three spatial dimensions.
- `anchor`: A two dimensional unit point within the view about which to   perform the rotation. The default value is  .
- `anchorZ`: The location on the z-axis around which to rotate the   content. The default is  .
- `perspective`: The relative vanishing point for the rotation. The   default is  .

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
- [enum ContentMode](contentmode.md)
  Constants that define how a view’s content fills the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/rotation3deffect(_:axis:anchor:anchorz:perspective:))*