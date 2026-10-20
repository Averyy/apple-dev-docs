# bones

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The control nodes of the animation skeleton.

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
var bones: [SCNNode] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SCNNode *> * bones;
```

#### Discussion

An array of [`SCNNode`](../scnnode.md) objects, each of which represents a control point of the animation skeleton. Moving a node deforms the surface of the skinner’s geometry, based on the skeleton data from which the skinner object was created.

## See Also

### Working with an Animation Skeleton
- [var skeleton: SCNNode?](./skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var boneInverseBindTransforms: [NSValue]?](./boneinversebindtransforms.md)
  The default transforms for the animation skeleton’s bone nodes.
- [var boneWeights: SCNGeometrySource](./boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](./boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/bones)*