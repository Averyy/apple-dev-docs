# simdWorldPosition

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
var simdWorldPosition: simd_float3 { get set }
```

#### Discussion

This vector isolates the translational aspect of the node’s [`simdWorldTransform`](scnnode/simdworldtransform.md) matrix, which in turn is the conversion of the node’s [`simdTransform`](scnnode/simdtransform.md) from local space to the scene’s world coordinate space. That is, it expresses the x, y, and z offsets of the node’s position from that of the scene’s [`rootNode`](scnscene/rootnode.md), and is equivalent to reading the node’s [`simdPosition`](scnnode/simdposition.md) vector and converting it to world space with the [`simdConvertPosition(_:from:)`](scnnode/simdconvertposition(_:from:).md) or [`simdConvertPosition(_:to:)`](scnnode/simdconvertposition(_:to:).md) method.

## See Also

- [var worldPosition: SCNVector3](scnnode/worldposition.md)
  The node’s position relative to the scene’s world coordinate space.
- [var simdWorldTransform: simd_float4x4](scnnode/simdworldtransform.md)
  The world transform applied to the node.
- [var simdWorldOrientation: simd_quatf](scnnode/simdworldorientation.md)
  The node’s orientation relative to the scene’s world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldposition)*