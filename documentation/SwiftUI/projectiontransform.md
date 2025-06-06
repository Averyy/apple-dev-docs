# ProjectionTransform

**Framework**: SwiftUI  
**Kind**: struct

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
struct ProjectionTransform
```

## Topics

### Creating a transform
- [init()](projectiontransform/init.md)
- [init(_:)](projectiontransform/init(_:).md)
### Getting transform characteristics
- [var isAffine: Bool](projectiontransform/isaffine.md)
- [var isIdentity: Bool](projectiontransform/isidentity.md)
### Manipulating transforms
- [func invert() -> Bool](projectiontransform/invert.md)
- [func inverted() -> ProjectionTransform](projectiontransform/inverted.md)
- [func concatenating(ProjectionTransform) -> ProjectionTransform](projectiontransform/concatenating(_:).md)
### Accessing the transform’s coefficients
- [var m11: CGFloat](projectiontransform/m11.md)
- [var m12: CGFloat](projectiontransform/m12.md)
- [var m13: CGFloat](projectiontransform/m13.md)
- [var m21: CGFloat](projectiontransform/m21.md)
- [var m22: CGFloat](projectiontransform/m22.md)
- [var m23: CGFloat](projectiontransform/m23.md)
- [var m31: CGFloat](projectiontransform/m31.md)
- [var m32: CGFloat](projectiontransform/m32.md)
- [var m33: CGFloat](projectiontransform/m33.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

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
  Scales this view by the specified horizontal, vertical, and depth factors.
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
  Applies a 3D transformation to the receiver.
- [func projectionEffect(ProjectionTransform) -> some View](view/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [enum ContentMode](contentmode.md)
  Constants that define how a view’s content fills the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/projectiontransform)*