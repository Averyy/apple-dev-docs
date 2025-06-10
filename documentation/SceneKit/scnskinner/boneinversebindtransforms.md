# boneInverseBindTransforms

**Framework**: SceneKit  
**Kind**: property

The default transforms for the animation skeleton’s bone nodes.

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
var boneInverseBindTransforms: [NSValue]? { get }
```

#### Discussion

An array of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects containing [`SCNMatrix4`](scnmatrix4-swift.struct.md) transforms, each of which corresponds to a node in the [`bones`](scnskinner/bones.md) array. Each value is the inverse of the bone node’s transform from bind space (that is, of the concatenation of all transforms from the skeleton root down to that bone) in the skeleton’s default pose.

## See Also

- [var skeleton: SCNNode?](scnskinner/skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var bones: [SCNNode]](scnskinner/bones.md)
  The control nodes of the animation skeleton.
- [var boneWeights: SCNGeometrySource](scnskinner/boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](scnskinner/boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/boneinversebindtransforms)*