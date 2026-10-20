# simdPivot

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The pivot point for the node’s position, rotation, and scale. Animatable.

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
var simdPivot: simd_float4x4 { get set }
```

```objc
@property (nonatomic) simd_float4x4 simdPivot;
```

#### Discussion

A node’s pivot is the transform between its coordinate space and that used by its [`simdPosition`](./simdposition.md), [`simdRotation`](./simdrotation.md), and [`simdScale`](./simdscale.md) properties. The default pivot is the identity matrix, specifying that the node’s position locates the origin of its coordinate system, its rotation is about an axis through its center, and its scale is also relative to that center point.

Changing the pivot transform alters these behaviors in many useful ways. You can:

- Offset the node’s contents relative to its position. For example, by setting the pivot to a translation transform you can position a node containing a sphere geometry relative to where the sphere would rest on a floor instead of relative to its center.
- Move the node’s axis of rotation. For example, with a translation transform you can cause a node to revolve around a faraway point instead of rotating around its center, and with a rotation transform you can tilt the axis of rotation.
- Adjust the center point and direction for scaling the node. For example, with a translation transform you can cause a node to grow or shrink relative to a corner instead of to its center.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var pivot: SCNMatrix4](./pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.
### Managing the Node’s Transform
- [var simdTransform: simd_float4x4](./simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdpivot)*