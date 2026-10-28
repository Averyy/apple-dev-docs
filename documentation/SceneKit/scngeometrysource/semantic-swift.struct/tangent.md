# tangent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for surface tangent vector data.

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
static let tangent: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticTangent;
```

## Discussion

For a geometry source, this semantic identifies data containing the surface tangent vector at each vertex in the geometry. SceneKit uses this information to compute advanced lighting effects on the surface.

For a custom shader program, you use this semantic to bind SceneKit’s vertex tangent data to an input attribute of the shader.

Vertex tangent data is typically an array of three- or four-component vectors.

## See Also

### Advanced Shading Semantics
- [static let color: SCNGeometrySource.Semantic](./color.md)
  The semantic for per-vertex color data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/tangent)*