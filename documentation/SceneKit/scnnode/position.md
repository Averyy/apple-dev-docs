# position

**Framework**: SceneKit  
**Kind**: property

The translation applied to the node. Animatable.

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
var position: SCNVector3 { get set }
```

#### Discussion

The node’s position locates it within the coordinate system of its parent, as modified by the node’s [`pivot`](scnnode/pivot.md) property. The default position is the zero vector, indicating that the node is placed at the origin of the parent node’s coordinate system.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var simdPosition: simd_float3](scnnode/simdposition.md)
  The translation applied to the node. Animatable.
- [var transform: SCNMatrix4](scnnode/transform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var rotation: SCNVector4](scnnode/rotation.md)
  The node’s orientation, expressed as a rotation angle about an axis. Animatable.
- [var eulerAngles: SCNVector3](scnnode/eulerangles.md)
  The node’s orientation, expressed as pitch, yaw, and roll angles in radians. Animatable.
- [var orientation: SCNQuaternion](scnnode/orientation.md)
  The node’s orientation, expressed as a quaternion. Animatable.
- [var scale: SCNVector3](scnnode/scale.md)
  The scale factor applied to the node. Animatable.
- [var pivot: SCNMatrix4](scnnode/pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/position)*