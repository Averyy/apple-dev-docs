# skeleton

**Framework**: SceneKit  
**Kind**: property

The root node of the skinner object’s animation skeleton.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
weak var skeleton: SCNNode? { get set }
```

#### Discussion

If you replace a skinner’s skeleton by assigning a different node to this property, the new skeleton must have the same structure as the skeleton it replaces. That is, the hierarchy of nodes must match, although the current state of each node may not.

## See Also

- [var bones: [SCNNode]](scnskinner/bones.md)
  The control nodes of the animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](scnskinner/boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](scnskinner/boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](scnskinner/boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/skeleton)*