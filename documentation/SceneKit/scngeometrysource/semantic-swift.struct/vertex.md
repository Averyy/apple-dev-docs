# vertex

**Framework**: SceneKit  
**Kind**: property

The semantic for vertex position data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let vertex: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing the positions of each vertex in the geometry. If you create a custom geometry using the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) method, you must provide a geometry source for this semantic.

For a custom shader program, you use this semantic to bind SceneKit’s vertex position data to an input attribute of the shader.

Vertex position data is typically an array of three- or four-component vectors.

## See Also

- [static let normal: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/normal.md)
  The semantic for surface normal data.
- [static let texcoord: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/texcoord.md)
  The semantic for texture coordinate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/vertex)*