# simdWorldTransform

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The world transform applied to the node.

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
var simdWorldTransform: simd_float4x4 { get set }
```

```objc
@property (nonatomic) simd_float4x4 simdWorldTransform;
```

#### Discussion

A world transform is the node’s coordinate space transform relative to the scene’s coordinate space. This transform is the concatenation of the node’s [`simdTransform`](./simdtransform.md) property with that of its parent node, the parent’s parent, and so on up to the [`rootNode`](../scnscene/rootnode.md) object of the scene.

## See Also

### Related Documentation
- [var worldTransform: SCNMatrix4](./worldtransform.md)
  The world transform applied to the node.
- [var parent: SCNNode?](./parent.md)
  The node’s parent in the scene graph hierarchy.
### Managing Transforms in World Space
- [var simdWorldOrientation: simd_quatf](./simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var simdWorldPosition: simd_float3](./simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldtransform)*