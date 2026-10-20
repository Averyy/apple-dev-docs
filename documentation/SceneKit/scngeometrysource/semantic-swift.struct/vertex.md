# vertex

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for vertex position data.

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
static let vertex: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticVertex;
```

#### Discussion

For a geometry source, this semantic identifies data containing the positions of each vertex in the geometry. If you create a custom geometry using the [`init(sources:elements:)`](../../scngeometry/init%28sources,elements%29.md) method, you must provide a geometry source for this semantic.

For a custom shader program, you use this semantic to bind SceneKit’s vertex position data to an input attribute of the shader.

Vertex position data is typically an array of three- or four-component vectors.

## See Also

### Basic Geometry Semantics
- [static let normal: SCNGeometrySource.Semantic](./normal.md)
  The semantic for surface normal data.
- [static let texcoord: SCNGeometrySource.Semantic](./texcoord.md)
  The semantic for texture coordinate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/vertex)*