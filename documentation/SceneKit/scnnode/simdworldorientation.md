# simdWorldOrientation

**Framework**: SceneKit  
**Kind**: property

The node’s orientation relative to the scene’s world coordinate space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var simdWorldOrientation: simd_quatf { get set }
```

#### Discussion

This quaternion isolates the rotational aspect of the node’s [`simdWorldTransform`](scnnode/simdworldtransform.md) matrix, which in turn is the conversion of the node’s [`simdTransform`](scnnode/simdtransform.md) from local space to the scene’s world coordinate space. That is, it expresses the difference in axis and angle of rotation between the node and the scene’s [`rootNode`](scnscene/rootnode.md).

## See Also

- [var worldOrientation: SCNQuaternion](scnnode/worldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.
- [var simdWorldTransform: simd_float4x4](scnnode/simdworldtransform.md)
  The world transform applied to the node.
- [var simdWorldPosition: simd_float3](scnnode/simdworldposition.md)
  The node’s position relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldorientation)*