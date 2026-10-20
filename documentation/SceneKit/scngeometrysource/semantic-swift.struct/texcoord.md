# texcoord

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for texture coordinate data.

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
static let texcoord: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticTexcoord;
```

#### Discussion

For a geometry source, this semantic identifies data containing texture mapping coordinates for each vertex in the geometry. Unlike other semantics, a geometry may contain multiple sources for texture coordinates—each corresponds to a separate [`mappingChannel`](../../scnmaterialproperty/mappingchannel.md) number that you can use when associating textured materials.

For a custom shader program, you use this semantic to bind SceneKit’s texture coordinate data to one or more input attributes of the shader.

Texture coordinate data is typically an array of two-component vectors.

## See Also

### Basic Geometry Semantics
- [static let vertex: SCNGeometrySource.Semantic](./vertex.md)
  The semantic for vertex position data.
- [static let normal: SCNGeometrySource.Semantic](./normal.md)
  The semantic for surface normal data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/texcoord)*