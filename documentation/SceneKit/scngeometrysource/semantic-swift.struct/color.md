# color

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for per-vertex color data.

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
static let color: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticColor;
```

## Discussion

For a geometry source, this semantic identifies data containing a color for each vertex in the geometry. SceneKit interpolates per-vertex colors across a surface to produce smooth shading. Per-vertex colors modulate those produced by lighting and a geometry’s materials, if applicable.

For a custom shader program, you use this semantic to bind SceneKit’s vertex color data to an input attribute of the shader.

Vertex color data is typically an array of three- or four-component vectors.

## See Also

### Advanced Shading Semantics
- [static let tangent: SCNGeometrySource.Semantic](./tangent.md)
  The semantic for surface tangent vector data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/color)*