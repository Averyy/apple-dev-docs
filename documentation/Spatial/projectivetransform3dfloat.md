# ProjectiveTransform3DFloat

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

A single-precision 3D projective transformation matrix.

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
struct ProjectiveTransform3DFloat
```

```c
typedef struct { ... } SPProjectiveTransform3DFloat;
```

## Topics

### Operators
- [static func * (ProjectiveTransform3DFloat, ProjectiveTransform3DFloat) -> ProjectiveTransform3DFloat](./projectivetransform3dfloat/star%28_,_%29.md)
  Returns the product of two projective transforms.
- [static func *= (inout ProjectiveTransform3DFloat, ProjectiveTransform3DFloat)](./projectivetransform3dfloat/stareq%28_,_%29.md)
  Calculates the concatenation of two projective transforms and stores the result in the left-hand-side variable.
### Initializers
- [init()](./projectivetransform3dfloat/init%28%29-89m3y.md)
  Returns a new identity projective transform.
- [init()](./projectivetransform3dfloat/init%28%29-c35e.md)
  Returns a new identity projective transform.
- [init(simd_double4x4)](./projectivetransform3dfloat/init%28_%29-43p4e.md)
  Returns a new affine transform structure from the specified double-precision 4 x 3 matrix.
- [init(simd_float4x4)](./projectivetransform3dfloat/init%28_%29-56itt.md)
  Returns a new transform from the specified 4 x 4 matrix.
- [init(AffineTransform3DFloat)](./projectivetransform3dfloat/init%28_%29-6ffxa.md)
  Returns a new transform from the specified affine transform.
- [init(ProjectiveTransform3D)](./projectivetransform3dfloat/init%28_%29-9r5ov.md)
  Returns a single-precision projective transformation from a double-precision projective transformation.
- [init(fovY: Angle2DFloat, aspectRatio: Float, nearZ: Float, farZ: Float)](./projectivetransform3dfloat/init%28fovy,aspectratio,nearz,farz%29.md)
- [init(fovY: Angle2DFloat, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool)](./projectivetransform3dfloat/init%28fovy,aspectratio,nearz,farz,reversez%29.md)
- [init(leftTangent: Float, rightTangent: Float, topTangent: Float, bottomTangent: Float, nearZ: Float, farZ: Float, reverseZ: Bool)](./projectivetransform3dfloat/init%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
- [init(matrix: simd_float4x4)](./projectivetransform3dfloat/init%28matrix%29.md)
- [init(pose: Pose3DFloat)](./projectivetransform3dfloat/init%28pose%29.md)
  Returns a new transform from the specified pose.
- [init(scaledPose: ScaledPose3DFloat)](./projectivetransform3dfloat/init%28scaledpose%29.md)
  Returns a new transform from the specified scaled pose.
### Instance Properties
- [var isAffine: Bool](./projectivetransform3dfloat/isaffine.md)
- [var isInvertible: Bool](./projectivetransform3dfloat/isinvertible.md)
- [var matrix: simd_float4x4](./projectivetransform3dfloat/matrix.md)
- [var scaleComponent: Size3DFloat](./projectivetransform3dfloat/scalecomponent.md)
  The projective transform’s scale component.
### Instance Methods
- [func is3DFloatProjection() -> Bool](./projectivetransform3dfloat/is3dfloatprojection%28%29.md)
### Default Implementations
- [CustomReflectable Implementations](./projectivetransform3dfloat/customreflectable-implementations.md)
- [Scalable3DProtocol Implementations](./projectivetransform3dfloat/scalable3dprotocol-implementations.md)
- [Shearable3DProtocol Implementations](./projectivetransform3dfloat/shearable3dprotocol-implementations.md)
- [Transform3DProtocol Implementations](./projectivetransform3dfloat/transform3dprotocol-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Rotatable3DProtocol](./rotatable3dprotocol.md)
- [Scalable3DProtocol](./scalable3dprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Shearable3DProtocol](./shearable3dprotocol.md)
- [SpatialTypeProtocol](./spatialtypeprotocol.md)
- [Transform3DProtocol](./transform3dprotocol.md)
- [Translatable3DProtocol](./translatable3dprotocol.md)

## See Also

### Affine and projective transforms
- [struct AffineTransform3D](./affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct AffineTransform3DFloat](./affinetransform3dfloat.md)
- [struct ProjectiveTransform3D](./projectivetransform3d.md)
  A 3D projective transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat)*