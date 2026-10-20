# worldOrientation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The node’s orientation relative to the scene’s world coordinate space.

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
var worldOrientation: SCNQuaternion { get set }
```

```objc
@property (nonatomic) SCNQuaternion worldOrientation;
```

#### Discussion

This quaternion isolates the rotational aspect of the node’s [`worldTransform`](./worldtransform.md) matrix, which in turn is the conversion of the node’s [`transform`](./transform.md) from local space to the scene’s world coordinate space. That is, it expresses the difference in axis and angle of rotation between the node and the scene’s [`rootNode`](../scnscene/rootnode.md).

## See Also

### Related Documentation
- [var simdWorldOrientation: simd_quatf](./simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
### Managing Transforms in World Space (SceneKit Types)
- [var worldTransform: SCNMatrix4](./worldtransform.md)
  The world transform applied to the node.
- [func setWorldTransform(SCNMatrix4)](./setworldtransform%28_%29.md)
  Sets the world transform applied to the node.
- [var worldPosition: SCNVector3](./worldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldorientation)*