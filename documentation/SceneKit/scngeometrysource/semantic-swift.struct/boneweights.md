# boneWeights

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for bone weight data, used for skeletal animation of skinned surfaces.

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
static let boneWeights: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticBoneWeights;
```

## Discussion

For a geometry source, this semantic identifies data containing skeletal animation data for each vertex in the geometry. SceneKit uses this information to determine how much a vertex’s position is influenced by the positions of bone nodes in the skeleton.

For a custom shader program, you use this semantic to bind SceneKit’s bone weight data to an input attribute of the shader.

For details on skeletal animation, see [`SCNSkinner`](../../scnskinner.md).

## See Also

### Skeletal Animation Semantics
- [static let boneIndices: SCNGeometrySource.Semantic](./boneindices.md)
  The semantic for bone index data, used for skeletal animation of skinned surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/boneweights)*