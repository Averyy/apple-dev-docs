# simdPosition

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The translation applied to the node. Animatable.

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
var simdPosition: simd_float3 { get set }
```

```objc
@property (nonatomic) simd_float3 simdPosition;
```

## Discussion

The node’s position locates it within the coordinate system of its parent, as modified by the node’s [`simdPivot`](./simdpivot.md) property. The default position is the zero vector, indicating that the node is placed at the origin of the parent node’s coordinate system.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var position: SCNVector3](./position.md)
  The translation applied to the node. Animatable.
### Managing the Node’s Transform
- [var simdTransform: simd_float4x4](./simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdposition)*