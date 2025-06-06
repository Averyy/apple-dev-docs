# transform

**Framework**: SceneKit  
**Kind**: property

The transform applied to the node relative to its parent. Animatable.

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
var transform: SCNMatrix4 { get set }
```

#### Discussion

The transformation is the combination of the node’s [`rotation`](scnnode/rotation.md), [`position`](scnnode/position.md), and [`scale`](scnnode/scale.md) properties. The default transformation is [`SCNMatrix4Identity`](scnmatrix4identity.md).

When you set the value of this property, the node’s [`rotation`](scnnode/rotation.md), [`orientation`](scnnode/orientation.md), [`eulerAngles`](scnnode/eulerangles.md), [`position`](scnnode/position.md), and [`scale`](scnnode/scale.md) properties automatically change to match the new transform, and vice versa. SceneKit can perform this conversion only if the transform you provide is a combination of rotation, translation, and scale operations. If you set the value of this property to a skew transformation or to a nonaffine transformation, the values of these properties become undefined. Setting a new value for any of these properties causes SceneKit to compute a new transformation, discarding any skew or nonaffine operations in the original transformation.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var simdTransform: simd_float4x4](scnnode/simdtransform.md)
  The transform applied to the node relative to its parent. Animatable.
- [var position: SCNVector3](scnnode/position.md)
  The translation applied to the node. Animatable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/transform)*