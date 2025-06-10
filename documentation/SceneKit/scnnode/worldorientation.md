# worldOrientation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation relative to the scene’s world coordinate space.

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
var worldOrientation: SCNQuaternion { get set }
```

#### Discussion

This quaternion isolates the rotational aspect of the node’s [`worldTransform`](scnnode/worldtransform.md) matrix, which in turn is the conversion of the node’s [`transform`](scnnode/transform.md) from local space to the scene’s world coordinate space. That is, it expresses the difference in axis and angle of rotation between the node and the scene’s [`rootNode`](scnscene/rootnode.md).

## See Also

- [var simdWorldOrientation: simd_quatf](scnnode/simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var worldTransform: SCNMatrix4](scnnode/worldtransform.md)
  The world transform applied to the node.
- [func setWorldTransform(SCNMatrix4)](scnnode/setworldtransform(_:).md)
  Sets the world transform applied to the node.
- [var worldPosition: SCNVector3](scnnode/worldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldorientation)*