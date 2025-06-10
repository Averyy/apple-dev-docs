# boneIndices

**Framework**: SceneKit  
**Kind**: property

The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.

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
var boneIndices: SCNGeometrySource { get }
```

#### Discussion

This geometry source’s [`semantic`](scngeometrysource/semantic-swift.property.md) property must be [`boneIndices`](scngeometrysource/semantic-swift.struct/boneindices.md). Its data is an array of integer vectors, each of which corresponds to a weight vector in the [`boneWeights`](scnskinner/boneweights.md) geometry source. Each component in a vector specifies the index of the node in the [`bones`](scnskinner/bones.md) array for the corresponding bone weight component.

## See Also

- [var skeleton: SCNNode?](scnskinner/skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var bones: [SCNNode]](scnskinner/bones.md)
  The control nodes of the animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](scnskinner/boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](scnskinner/boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/boneindices)*