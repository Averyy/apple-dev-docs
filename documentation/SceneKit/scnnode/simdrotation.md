# simdRotation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation, expressed as a rotation angle about an axis. Animatable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var simdRotation: simd_float4 { get set }
```

#### Discussion

The four-component rotation vector specifies the direction of the rotation axis in the first three components and the angle of rotation (in radians) in the fourth. The default rotation is the zero vector, specifying no rotation. Rotation is applied relative to the node’s [`simdPivot`](scnnode/simdpivot.md) property.

The [`simdRotation`](scnnode/simdrotation.md), [`simdEulerAngles`](scnnode/simdeulerangles.md), and [`simdOrientation`](scnnode/simdorientation.md) properties all affect the rotational aspect of the node’s [`simdTransform`](scnnode/simdtransform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var rotation: SCNVector4](scnnode/rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var simdTransform: simd_float4x4](scnnode/simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var simdPosition: simd_float3](scnnode/simdposition.md)
  The translation applied to the node. Animatable.
- [var simdEulerAngles: simd_float3](scnnode/simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdOrientation: simd_quatf](scnnode/simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdScale: simd_float3](scnnode/simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](scnnode/simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdrotation)*