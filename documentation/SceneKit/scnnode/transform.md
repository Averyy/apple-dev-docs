# transform

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
var transform: SCNMatrix4 { get set }
```

```objc
@property (nonatomic) SCNMatrix4 transform;
```

#### Discussion

The transformation is the combination of the node’s [`rotation`](./rotation.md), [`position`](./position.md), and [`scale`](./scale.md) properties. The default transformation is [`SCNMatrix4Identity`](../scnmatrix4identity.md).

When you set the value of this property, the node’s [`rotation`](./rotation.md), [`orientation`](./orientation.md), [`eulerAngles`](./eulerangles.md), [`position`](./position.md), and [`scale`](./scale.md) properties automatically change to match the new transform, and vice versa. SceneKit can perform this conversion only if the transform you provide is a combination of rotation, translation, and scale operations. If you set the value of this property to a skew transformation or to a nonaffine transformation, the values of these properties become undefined. Setting a new value for any of these properties causes SceneKit to compute a new transformation, discarding any skew or nonaffine operations in the original transformation.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var simdTransform: simd_float4x4](./simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
### Managing the Node’s Transform (SceneKit Types)
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
- [var pivot: SCNMatrix4](./pivot.md)
  The pivot point for the node’s position, rotation, and scale. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/transform)*