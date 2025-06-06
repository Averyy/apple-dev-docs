# orientation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation, expressed as a quaternion. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var orientation: SCNQuaternion { get set }
```

#### Discussion

The [`rotation`](scnnode/rotation.md), [`eulerAngles`](scnnode/eulerangles.md), and [`orientation`](scnnode/orientation.md) properties all affect the rotational aspect of the node’s [`transform`](scnnode/transform.md) property. Any change to one of these properties is reflected in the others.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var simdOrientation: simd_quatf](scnnode/simdorientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var transform: SCNMatrix4](scnnode/transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](scnnode/position.md)
  The translation applied to the node. Animatable.
- [var rotation: SCNVector4](scnnode/rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var eulerAngles: SCNVector3](scnnode/eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var scale: SCNVector3](scnnode/scale.md)
  The scale factor applied to the node. Animatable.
- [var pivot: SCNMatrix4](scnnode/pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/orientation)*