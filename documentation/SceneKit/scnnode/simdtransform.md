# simdTransform

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The transform applied to the node relative to its parent. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var simdTransform: simd_float4x4 { get set }
```

```objc
@property (nonatomic) simd_float4x4 simdTransform;
```

#### Discussion

The transform is the combination of the node’s [`simdRotation`](./simdrotation.md), [`simdPosition`](./simdposition.md), and [`simdScale`](./simdscale.md) properties. The default transform is the identity matrix.

When you set the value of this property, the node’s [`simdRotation`](./simdrotation.md), [`simdOrientation`](./simdorientation.md), [`simdEulerAngles`](./simdeulerangles.md), [`simdPosition`](./simdposition.md), and [`simdScale`](./simdscale.md) properties automatically change to match the new transform, and vice versa. SceneKit can perform this conversion only if the transform you provide is a combination of rotation, translation, and scale operations. If you set the value of this property to a skew transform or to a nonaffine transform, the values of these properties become undefined. Setting a new value for any of these properties causes SceneKit to compute a new transform, discarding any skew or nonaffine operations in the original transform.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var transform: SCNMatrix4](./transform.md)
  The transform applied to the node relative to its parent. Animatable.
### Managing the Node’s Transform
- [var simdPosition: simd_float3](./simdposition.md)
  The translation applied to the node. Animatable.
- [var simdRotation: simd_float4](./simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var simdEulerAngles: simd_float3](./simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdOrientation: simd_quatf](./simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdScale: simd_float3](./simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](./simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdtransform)*