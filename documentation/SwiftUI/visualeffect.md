# VisualEffect

**Framework**: SwiftUI  
**Kind**: protocol

Visual Effects change the visual appearance of a view without changing its ancestors or descendents.

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
protocol VisualEffect : Sendable, Animatable
```

#### Overview

Because effects do not impact layout, they are safe to use in situations where layout modification is not allowed. For example, effects may be applied as a function of position, accessed through a geometry proxy:

```swift
var body: some View {
    ContentRow()
        .visualEffect { content, geometryProxy in
            content.offset(x: geometryProxy.frame(in: .global).origin.y)
        }
}
```

You don’t conform to this protocol yourself. Instead, visual effects are created by calling modifier functions (such as `.offset(x:y:)` on other effects, as seen in the example above.

## Topics

### Adjusting Color
- [func brightness(Double) -> some VisualEffect](visualeffect/brightness(_:).md)
  Brightens the view by the specified amount.
- [func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect](visualeffect/coloreffect(_:isenabled:).md)
  Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func contrast(Double) -> some VisualEffect](visualeffect/contrast(_:).md)
  Sets the contrast and separation between similar colors in the view.
- [func grayscale(Double) -> some VisualEffect](visualeffect/grayscale(_:).md)
  Adds a grayscale effect to the view.
- [func hueRotation(Angle) -> some VisualEffect](visualeffect/huerotation(_:).md)
  Applies a hue rotation effect to the view.
- [func saturation(Double) -> some VisualEffect](visualeffect/saturation(_:).md)
  Adjusts the color saturation of the view.
- [func opacity(Double) -> some VisualEffect](visualeffect/opacity(_:).md)
  Sets the transparency of the view.
### Scaling
- [func scaleEffect(_:anchor:)](visualeffect/scaleeffect(_:anchor:).md)
  Scales this view uniformly by the specified factor.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some VisualEffect](visualeffect/scaleeffect(x:y:anchor:).md)
  Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors.
### Rotating
- [func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect](visualeffect/rotationeffect(_:anchor:).md)
  Rotates content in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some VisualEffect](visualeffect/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect](visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/rotation3deffect(_:anchor:).md)
  Rotates content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](visualeffect/rotation3deffect(_:axis:anchor:).md)
  Rotates content by an angle about an axis that you specify as a tuple of elements.
### Translating
- [func offset(CGSize) -> some VisualEffect](visualeffect/offset(_:).md)
  Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some VisualEffect](visualeffect/offset(x:y:).md)
  Offsets the view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some VisualEffect](visualeffect/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
### Applying a transform
- [func transform3DEffect(AffineTransform3D) -> some VisualEffect](visualeffect/transform3deffect(_:).md)
  Applies a 3D transformation to the receiver.
- [func transformEffect(_:)](visualeffect/transformeffect(_:).md)
  Applies an affine transformation to the view’s rendered output.
### Applying other effects
- [func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect](visualeffect/blur(radius:opaque:).md)
  Applies a Gaussian blur to the view.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some VisualEffect](visualeffect/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new visual effect that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some VisualEffect](visualeffect/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new visual effect that applies `shader` to `self` as a filter on the raster layer created from `self`.
### Instance Methods
- [func blendMode(BlendMode) -> some VisualEffect](visualeffect/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.

## Relationships

### Inherits From
- [Animatable](animatable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [EmptyVisualEffect](emptyvisualeffect.md)

## See Also

- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](view/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](view/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [struct EmptyVisualEffect](emptyvisualeffect.md)
  The base visual effect that you apply additional effect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect)*