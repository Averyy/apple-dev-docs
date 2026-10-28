# scale

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The scale factor applied to the node. Animatable.

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
var scale: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 scale;
```

## Discussion

Each component of the scale vector multiplies the corresponding dimension of the node’s geometry. The default scale is `1.0` in all three dimensions. For example, applying a scale of (2.0, 0.5, 2.0) to a node containing a cube geometry reduces its height and increases its width and depth. Scaling is applied relative to the node’s [`pivot`](./pivot.md) property.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var simdScale: simd_float3](./simdscale.md)
  The scale factor applied to the node. Animatable.
### Managing the Node’s Transform (SceneKit Types)
- [var transform: SCNMatrix4](./transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](./position.md)
  The translation applied to the node. Animatable.
- [var rotation: SCNVector4](./rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var eulerAngles: SCNVector3](./eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var orientation: SCNQuaternion](./orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var pivot: SCNMatrix4](./pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/scale)*