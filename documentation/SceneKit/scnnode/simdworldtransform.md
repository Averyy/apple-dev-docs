# simdWorldTransform

**Framework**: SceneKit  
**Kind**: property

The world transform applied to the node.

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
var simdWorldTransform: simd_float4x4 { get set }
```

#### Discussion

A world transform is the node’s coordinate space transform relative to the scene’s coordinate space. This transform is the concatenation of the node’s [`simdTransform`](scnnode/simdtransform.md) property with that of its parent node, the parent’s parent, and so on up to the [`rootNode`](scnscene/rootnode.md) object of the scene.

## See Also

- [var worldTransform: SCNMatrix4](scnnode/worldtransform.md)
  The world transform applied to the node.
- [var parent: SCNNode?](scnnode/parent.md)
  The node’s parent in the scene graph hierarchy.
- [var simdWorldOrientation: simd_quatf](scnnode/simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var simdWorldPosition: simd_float3](scnnode/simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldtransform)*