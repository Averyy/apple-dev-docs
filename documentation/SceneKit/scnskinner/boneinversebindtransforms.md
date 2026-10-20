# boneInverseBindTransforms

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The default transforms for the animation skeleton’s bone nodes.

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
var boneInverseBindTransforms: [NSValue]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSValue *> * boneInverseBindTransforms;
```

#### Discussion

An array of [`NSValue`](../../Foundation/nsvalue.md) objects containing [`SCNMatrix4`](../scnmatrix4-swift.struct.md) transforms, each of which corresponds to a node in the [`bones`](./bones.md) array. Each value is the inverse of the bone node’s transform from bind space (that is, of the concatenation of all transforms from the skeleton root down to that bone) in the skeleton’s default pose.

## See Also

### Working with an Animation Skeleton
- [var skeleton: SCNNode?](./skeleton.md)
  The root node of the skinner object’s animation skeleton.
- [var bones: [SCNNode]](./bones.md)
  The control nodes of the animation skeleton.
- [var boneWeights: SCNGeometrySource](./boneweights.md)
  The geometry source that defines the influence of each bone on the positions the geometry’s vertices.
- [var boneIndices: SCNGeometrySource](./boneindices.md)
  The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/boneinversebindtransforms)*