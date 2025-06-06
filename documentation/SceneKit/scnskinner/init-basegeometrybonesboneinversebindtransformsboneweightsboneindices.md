# init(baseGeometry:bones:boneInverseBindTransforms:boneWeights:boneIndices:)

**Framework**: SceneKit  
**Kind**: init

Creates a skinner object with the specified visible geometry and skeleton information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(baseGeometry: SCNGeometry?, bones: [SCNNode], boneInverseBindTransforms: [NSValue]?, boneWeights: SCNGeometrySource, boneIndices: SCNGeometrySource)
```

#### Return Value

A new skinner object.

#### Discussion

To use the skinner object in a scene, assign it to the [`skinner`](scnnode/skinner.md) property of a node. That node’s [`geometry`](scnnode/geometry.md) property should reference the same [`SCNGeometry`](scngeometry.md) object as the skinner’s [`baseGeometry`](scnskinner/basegeometry.md) property.

## Parameters

- `baseGeometry`: The geometry whose surface the skinner’s animation skeleton deforms.
- `bones`: An array of   objects, each representing a bone or control point for the animation skeleton.
- `boneInverseBindTransforms`: An array of   objects containing   transforms, each of which corresponds to a node in the   array. Each value is the inverse of the bone node’s transform from bind space (that is, of the concatenation of all transforms from the skeleton root down to that bone) in the skeleton’s default pose.
- `boneWeights`: The geometry source defining the influence of each bone on the positions of vertices in the geometry. For details, see the   property.
- `boneIndices`: The geometry source defining the mapping from bone indices in skeleton data to the skinner’s bones array. For details, see the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/init(basegeometry:bones:boneinversebindtransforms:boneweights:boneindices:))*