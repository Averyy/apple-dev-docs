# boneIndices

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.

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
var boneIndices: SCNGeometrySource { get }
```

```objc
@property (nonatomic, readonly) SCNGeometrySource * boneIndices;
```

#### Discussion

This geometry source’s [`semantic`](../scngeometrysource/semantic-swift.property.md) property must be [`boneIndices`](../scngeometrysource/semantic-swift.struct/boneindices.md). Its data is an array of integer vectors, each of which corresponds to a weight vector in the [`boneWeights`](./boneweights.md) geometry source. Each component in a vector specifies the index of the node in the [`bones`](./bones.md) array for the corresponding bone weight component.

## See Also

### Working with an Animation Skeleton
- [var skeleton: SCNNode?](./skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var bones: [SCNNode]](./bones.md)
  The control nodes of the animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](./boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](./boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/boneindices)*