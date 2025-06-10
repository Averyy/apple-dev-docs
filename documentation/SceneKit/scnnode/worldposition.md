# worldPosition

**Framework**: SceneKit  
**Kind**: property

The node’s position relative to the scene’s world coordinate space.

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
var worldPosition: SCNVector3 { get set }
```

#### Discussion

This vector isolates the translational aspect of the node’s [`worldTransform`](scnnode/worldtransform.md) matrix, which in turn is the conversion of the node’s [`transform`](scnnode/transform.md) from local space to the scene’s world coordinate space. That is, it expresses the x, y, and z offsets of the node’s position from that of the scene’s [`rootNode`](scnscene/rootnode.md), and is equivalent to reading the node’s [`position`](scnnode/position.md) vector and converting it to world space with the [`convertPosition(_:from:)`](scnnode/convertposition(_:from:).md) or [`convertPosition(_:to:)`](scnnode/convertposition(_:to:).md) method.

## See Also

- [var simdWorldPosition: simd_float3](scnnode/simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.
- [var worldTransform: SCNMatrix4](scnnode/worldtransform.md)
  The world transform applied to the node.
- [func setWorldTransform(SCNMatrix4)](scnnode/setworldtransform(_:).md)
  Sets the world transform applied to the node.
- [var worldOrientation: SCNQuaternion](scnnode/worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldposition)*