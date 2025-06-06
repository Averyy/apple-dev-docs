# worldTransform

**Framework**: Scenekit  
**Kind**: property

The world transform applied to the node.

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
var worldTransform: SCNMatrix4 { get }
```

#### Discussion

A world transform is the node’s coordinate space transform relative to the scene’s coordinate space. This transform is the concatenation of the node’s [`transform`](scnnode/transform.md) property with that of its parent node, the parent’s parent, and so on up to the [`rootNode`](scnscene/rootnode.md) object of the scene.

> **Note**:  In macOS 10.13, iOS 11, tvOS 11, or watchOS 4 (and later), you can set this value with the [`setWorldTransform(_:)`](scnnode/setworldtransform(_:).md) method.

## See Also

- [var simdWorldTransform: simd_float4x4](scnnode/simdworldtransform.md)
  The world transform applied to the node.
- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [func setWorldTransform(SCNMatrix4)](scnnode/setworldtransform(_:).md)
  Sets the world transform applied to the node.
- [var worldOrientation: SCNQuaternion](scnnode/worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var worldPosition: SCNVector3](scnnode/worldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldtransform)*