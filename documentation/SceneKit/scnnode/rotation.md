# rotation

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
var rotation: SCNVector4 { get set }
```

```objc
@property (nonatomic) SCNVector4 rotation;
```

## Discussion

The four-component rotation vector specifies the direction of the rotation axis in the first three components and the angle of rotation (in radians) in the fourth. The default rotation is the zero vector, specifying no rotation. Rotation is applied relative to the node’s [`pivot`](./pivot.md) property.

The [`rotation`](./rotation.md), [`eulerAngles`](./eulerangles.md), and [`orientation`](./orientation.md) properties all affect the rotational aspect of the node’s [`transform`](./transform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var simdRotation: simd_float4](./simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
### Managing the Node’s Transform (SceneKit Types)
- [var transform: SCNMatrix4](./transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](./position.md)
  The translation applied to the node. Animatable.
- [var eulerAngles: SCNVector3](./eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var orientation: SCNQuaternion](./orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var scale: SCNVector3](./scale.md)
  The scale factor applied to the node. Animatable.
- [var pivot: SCNMatrix4](./pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/rotation)*