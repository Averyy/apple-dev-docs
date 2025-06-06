# simdTransform

**Framework**: SceneKit  
**Kind**: property

The transform applied to the node relative to its parent. Animatable.

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
var simdTransform: simd_float4x4 { get set }
```

#### Discussion

The transform is the combination of the node’s [`simdRotation`](scnnode/simdrotation.md), [`simdPosition`](scnnode/simdposition.md), and [`simdScale`](scnnode/simdscale.md) properties. The default transform is the identity matrix.

When you set the value of this property, the node’s [`simdRotation`](scnnode/simdrotation.md), [`simdOrientation`](scnnode/simdorientation.md), [`simdEulerAngles`](scnnode/simdeulerangles.md), [`simdPosition`](scnnode/simdposition.md), and [`simdScale`](scnnode/simdscale.md) properties automatically change to match the new transform, and vice versa. SceneKit can perform this conversion only if the transform you provide is a combination of rotation, translation, and scale operations. If you set the value of this property to a skew transform or to a nonaffine transform, the values of these properties become undefined. Setting a new value for any of these properties causes SceneKit to compute a new transform, discarding any skew or nonaffine operations in the original transform.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var transform: SCNMatrix4](scnnode/transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var simdPosition: simd_float3](scnnode/simdposition.md)
  The translation applied to the node. Animatable.
- [var simdRotation: simd_float4](scnnode/simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var simdEulerAngles: simd_float3](scnnode/simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdOrientation: simd_quatf](scnnode/simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdScale: simd_float3](scnnode/simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](scnnode/simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdtransform)*