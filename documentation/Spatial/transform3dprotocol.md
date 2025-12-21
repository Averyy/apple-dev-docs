# Transform3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that are common to transforms.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol Transform3DProtocol : SpatialTypeProtocol
```

## Topics

### Initializers
- [init(rotation: Self.Rotation)](transform3dprotocol/init(rotation:).md)
  Returns a new rotation transform.
- [init(scale: Self.Size)](transform3dprotocol/init(scale:).md)
  Returns a new scale transform.
- [init(scale: Self.Size, rotation: Self.Rotation, translation: Self.Vector)](transform3dprotocol/init(scale:rotation:translation:).md)
  Returns a new scale, rotate, translate transform.
- [init(shear: Self.AxisEnumeration)](transform3dprotocol/init(shear:).md)
  Returns a new shear transform
- [init(translation: Self.Vector)](transform3dprotocol/init(translation:).md)
  Returns a new translate transform.
### Instance Properties
- [var inverse: Self?](transform3dprotocol/inverse.md)
  Returns a transform that’s constructed by inverting an existing transform.
- [var isIdentity: Bool](transform3dprotocol/isidentity.md)
  Returns `true` if the transform is the identity transform.
- [var isRectilinear: Bool](transform3dprotocol/isrectilinear.md)
  Returns `true` if the transform is rectilinear.
- [var isTranslation: Bool](transform3dprotocol/istranslation.md)
  Returns `true` if the transform is a translation.
- [var isUniform: Bool](transform3dprotocol/isuniform.md)
  Returns `true` if the transform is uniform over all dimensions.
- [var rotation: Self.Rotation?](transform3dprotocol/rotation.md)
  The transform’s rotation. This is `nil` if the transform isn’t scale-rotate-translate.
- [var translation: Self.Vector](transform3dprotocol/translation.md)
  The transform’s translation.
### Instance Methods
- [func concatenating(Self) -> Self](transform3dprotocol/concatenating(_:).md)
  Returns a transform that’s constructed by combining two existing transforms.
- [func flip(along: Axis3D)](transform3dprotocol/flip(along:).md)
  Flips the transform along the specified axis.
- [func flipped(along: Axis3D) -> Self](transform3dprotocol/flipped(along:).md)
  Returns the transform flipped along the specified axis.
- [func isApproximatelyEqual(to: Self, tolerance: Self.Scalar) -> Bool](transform3dprotocol/isapproximatelyequal(to:tolerance:).md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](transform3dprotocol/isuniform(overdimensions:).md)
  Returns `true` if the transform is uniform over the specified dimensions.
### Type Properties
- [static var identity: Self](transform3dprotocol/identity.md)
  Returns the identity transform.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [AffineTransform3DFloat](affinetransform3dfloat.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [ProjectiveTransform3DFloat](projectivetransform3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/transform3dprotocol)*