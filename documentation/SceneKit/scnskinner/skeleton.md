# skeleton

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The root node of the skinner object’s animation skeleton.

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
weak var skeleton: SCNNode? { get set }
```

```objc
@property (nonatomic, weak, nullable) SCNNode * skeleton;
```

#### Discussion

If you replace a skinner’s skeleton by assigning a different node to this property, the new skeleton must have the same structure as the skeleton it replaces. That is, the hierarchy of nodes must match, although the current state of each node may not.

## See Also

### Working with an Animation Skeleton
- [var bones: [SCNNode]](./bones.md)
  The control nodes of the animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](./boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](./boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](./boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/skeleton)*