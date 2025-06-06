# texcoord

**Framework**: SceneKit  
**Kind**: property

The semantic for texture coordinate data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let texcoord: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing texture mapping coordinates for each vertex in the geometry. Unlike other semantics, a geometry may contain multiple sources for texture coordinates—each corresponds to a separate [`mappingChannel`](scnmaterialproperty/mappingchannel.md) number that you can use when associating textured materials.

For a custom shader program, you use this semantic to bind SceneKit’s texture coordinate data to one or more input attributes of the shader.

Texture coordinate data is typically an array of two-component vectors.

## See Also

- [static let vertex: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/vertex.md)
  The semantic for vertex position data.
- [static let normal: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/normal.md)
  The semantic for surface normal data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/texcoord)*