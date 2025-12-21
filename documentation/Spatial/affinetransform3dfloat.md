# AffineTransform3DFloat

**Framework**: Spatial  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct AffineTransform3DFloat
```

#### Overview

A single-precision 3D affine transformation matrix.

## Topics

### Operators
- [static func * (AffineTransform3DFloat, AffineTransform3DFloat) -> AffineTransform3DFloat](affinetransform3dfloat/*(_:_:).md)
  Returns the concatenation of two affine transforms.
- [static func *= (inout AffineTransform3DFloat, AffineTransform3DFloat)](affinetransform3dfloat/*=(_:_:).md)
  Calculates the concatenation of two affine transforms and stores the result in the left-hand-side variable.
### Initializers
- [init()](affinetransform3dfloat/init-6ek9q.md)
  Returns a new identity affine transform.
- [init()](affinetransform3dfloat/init-8li4c.md)
  Returns a new identity affine transform.
- [init(AffineTransform3D)](affinetransform3dfloat/init(_:)-2c2os.md)
  Returns a single-precision affine transformation from a double-precision affine transformation.
- [init(simd_double4x3)](affinetransform3dfloat/init(_:)-3a23d.md)
  Returns a new affine transform structure from the specified double-precision 4 x 3 matrix.
- [init(simd_float4x3)](affinetransform3dfloat/init(_:)-5ajh4.md)
- [init(matrix: simd_float4x3)](affinetransform3dfloat/init(matrix:).md)
- [init(pose: Pose3DFloat)](affinetransform3dfloat/init(pose:).md)
  Returns a new transform from the specified pose.
- [init(scaledPose: ScaledPose3DFloat)](affinetransform3dfloat/init(scaledpose:).md)
  Returns a new transform from the specified scaled pose.
- [init(truncating: ProjectiveTransform3DFloat)](affinetransform3dfloat/init(truncating:)-1jfno.md)
- [init(truncating: simd_double4x4)](affinetransform3dfloat/init(truncating:)-7vabe.md)
  Returns a new affine transform from a double-precision 4 x 4 matrix truncated to a  4 x 3 matrix.
- [init(truncating: simd_float4x4)](affinetransform3dfloat/init(truncating:)-8jfn6.md)
### Instance Properties
- [var columns: (Vector3DFloat, Vector3DFloat, Vector3DFloat, Vector3DFloat)](affinetransform3dfloat/columns.md)
  The columns of the underlying matrix.
- [var isInvertible: Bool](affinetransform3dfloat/isinvertible.md)
- [var matrix: simd_float4x3](affinetransform3dfloat/matrix.md)
- [var matrix3x3: simd_float3x3](affinetransform3dfloat/matrix3x3.md)
- [var matrix4x4: simd_float4x4](affinetransform3dfloat/matrix4x4.md)
- [var scale: Size3DFloat](affinetransform3dfloat/scale.md)
### Instance Methods
- [func changeBasis(from: AffineTransform3DFloat, to: AffineTransform3DFloat) -> AffineTransform3DFloat?](affinetransform3dfloat/changebasis(from:to:).md)
  Returns a new affine transform structure by applying a change-of-basis.
### Default Implementations
- [CustomReflectable Implementations](affinetransform3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](affinetransform3dfloat/decodable-implementations.md)
- [Encodable Implementations](affinetransform3dfloat/encodable-implementations.md)
- [Equatable Implementations](affinetransform3dfloat/equatable-implementations.md)
- [Hashable Implementations](affinetransform3dfloat/hashable-implementations.md)
- [Scalable3DProtocol Implementations](affinetransform3dfloat/scalable3dprotocol-implementations.md)
- [Shearable3DProtocol Implementations](affinetransform3dfloat/shearable3dprotocol-implementations.md)
- [Transform3DProtocol Implementations](affinetransform3dfloat/transform3dprotocol-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shearable3DProtocol](shearable3dprotocol.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [Transform3DProtocol](transform3dprotocol.md)
- [Translatable3DProtocol](translatable3dprotocol.md)

## See Also

- [struct AffineTransform3D](affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct ProjectiveTransform3D](projectivetransform3d.md)
  A 3D projective transformation matrix.
- [struct ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat)*