# color

**Framework**: SceneKit  
**Kind**: property

The semantic for per-vertex color data.

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
static let color: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing a color for each vertex in the geometry. SceneKit interpolates per-vertex colors across a surface to produce smooth shading. Per-vertex colors modulate those produced by lighting and a geometry’s materials, if applicable.

For a custom shader program, you use this semantic to bind SceneKit’s vertex color data to an input attribute of the shader.

Vertex color data is typically an array of three- or four-component vectors.

## See Also

- [static let tangent: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/tangent.md)
  The semantic for surface tangent vector data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/color)*