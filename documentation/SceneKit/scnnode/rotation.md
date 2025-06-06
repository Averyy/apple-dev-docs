# rotation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation, expressed as a rotation angle about an axis. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var rotation: SCNVector4 { get set }
```

#### Discussion

The four-component rotation vector specifies the direction of the rotation axis in the first three components and the angle of rotation (in radians) in the fourth. The default rotation is the zero vector, specifying no rotation. Rotation is applied relative to the node’s [`pivot`](scnnode/pivot.md) property.

The [`rotation`](scnnode/rotation.md), [`eulerAngles`](scnnode/eulerangles.md), and [`orientation`](scnnode/orientation.md) properties all affect the rotational aspect of the node’s [`transform`](scnnode/transform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var simdRotation: simd_float4](scnnode/simdrotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var transform: SCNMatrix4](scnnode/transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](scnnode/position.md)
  The translation applied to the node. Animatable.
- [var eulerAngles: SCNVector3](scnnode/eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var orientation: SCNQuaternion](scnnode/orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var scale: SCNVector3](scnnode/scale.md)
  The scale factor applied to the node. Animatable.
- [var pivot: SCNMatrix4](scnnode/pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/rotation)*