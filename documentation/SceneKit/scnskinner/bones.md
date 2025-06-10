# bones

**Framework**: SceneKit  
**Kind**: property

The control nodes of the animation skeleton.

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
var bones: [SCNNode] { get }
```

#### Discussion

An array of [`SCNNode`](scnnode.md) objects, each of which represents a control point of the animation skeleton. Moving a node deforms the surface of the skinner’s geometry, based on the skeleton data from which the skinner object was created.

## See Also

- [var skeleton: SCNNode?](scnskinner/skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](scnskinner/boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](scnskinner/boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](scnskinner/boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/bones)*