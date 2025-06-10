# normal

**Framework**: SceneKit  
**Kind**: property

The semantic for surface normal data.

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
static let normal: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing the surface normal vector at each vertex in the geometry. SceneKit uses this information to compute lighting effects on the surface.

For a custom shader program, you use this semantic to bind SceneKit’s vertex normal data to an input attribute of the shader.

Vertex normal data is typically an array of three- or four-component vectors.

## See Also

- [static let vertex: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/vertex.md)
  The semantic for vertex position data.
- [static let texcoord: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/texcoord.md)
  The semantic for texture coordinate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/normal)*