# pivot

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
var pivot: SCNMatrix4 { get set }
```

```objc
@property (nonatomic) SCNMatrix4 pivot;
```

## Discussion

A node’s pivot is the transformation between its coordinate space and that used by its [`position`](./position.md), [`rotation`](./rotation.md), and [`scale`](./scale.md) properties. The default pivot is [`SCNMatrix4Identity`](../scnmatrix4identity.md), specifying that the node’s position locates the origin of its coordinate system, its rotation is about an axis through its center, and its scale is also relative to that center point.

Changing the pivot transform alters these behaviors in many useful ways. You can:

- Offset the node’s contents relative to its position. For example, by setting the pivot to a translation transform you can position a node containing a sphere geometry relative to where the sphere would rest on a floor instead of relative to its center.
- Move the node’s axis of rotation. For example, with a translation transform you can cause a node to revolve around a faraway point instead of rotating around its center, and with a rotation transform you can tilt the axis of rotation.
- Adjust the center point and direction for scaling the node. For example, with a translation transform you can cause a node to grow or shrink relative to a corner instead of to its center.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var simdPivot: simd_float4x4](./simdpivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.
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
- [var scale: SCNVector3](./scale.md)
  The scale factor applied to the node. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/pivot)*