# simdOrientation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation, expressed as a quaternion. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var simdOrientation: simd_quatf { get set }
```

#### Discussion

The [`simdRotation`](scnnode/simdrotation.md), [`simdEulerAngles`](scnnode/simdeulerangles.md), and [`simdOrientation`](scnnode/simdorientation.md) properties all affect the rotational aspect of the node’s [`simdTransform`](scnnode/simdtransform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var orientation: SCNQuaternion](scnnode/orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdTransform: simd_float4x4](scnnode/simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var simdPosition: simd_float3](scnnode/simdposition.md)
  The translation applied to the node. Animatable.
- [var simdRotation: simd_float4](scnnode/simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var simdEulerAngles: simd_float3](scnnode/simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdScale: simd_float3](scnnode/simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](scnnode/simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdorientation)*