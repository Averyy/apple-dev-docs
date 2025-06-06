# boneWeights

**Framework**: SceneKit  
**Kind**: property

The semantic for bone weight data, used for skeletal animation of skinned surfaces.

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
static let boneWeights: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing skeletal animation data for each vertex in the geometry. SceneKit uses this information to determine how much a vertex’s position is influenced by the positions of bone nodes in the skeleton.

For a custom shader program, you use this semantic to bind SceneKit’s bone weight data to an input attribute of the shader.

For details on skeletal animation, see [`SCNSkinner`](scnskinner.md).

## See Also

- [static let boneIndices: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/boneindices.md)
  The semantic for bone index data, used for skeletal animation of skinned surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/boneweights)*