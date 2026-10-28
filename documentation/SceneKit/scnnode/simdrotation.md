# simdRotation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The node’s orientation, expressed as a rotation angle about an axis. Animatable.

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
var simdRotation: simd_float4 { get set }
```

```objc
@property (nonatomic) simd_float4 simdRotation;
```

## Discussion

The four-component rotation vector specifies the direction of the rotation axis in the first three components and the angle of rotation (in radians) in the fourth. The default rotation is the zero vector, specifying no rotation. Rotation is applied relative to the node’s [`simdPivot`](./simdpivot.md) property.

The [`simdRotation`](./simdrotation.md), [`simdEulerAngles`](./simdeulerangles.md), and [`simdOrientation`](./simdorientation.md) properties all affect the rotational aspect of the node’s [`simdTransform`](./simdtransform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var rotation: SCNVector4](./rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
### Managing the Node’s Transform
- [var simdTransform: simd_float4x4](./simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var simdPosition: simd_float3](./simdposition.md)
  The translation applied to the node. Animatable.
- [var simdEulerAngles: simd_float3](./simdeulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var simdOrientation: simd_quatf](./simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var simdScale: simd_float3](./simdscale.md)
  The scale factor applied to the node. Animatable.
- [var simdPivot: simd_float4x4](./simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdrotation)*