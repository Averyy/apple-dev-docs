# tangent

**Framework**: SceneKit  
**Kind**: property

The semantic for surface tangent vector data.

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
static let tangent: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing the surface tangent vector at each vertex in the geometry. SceneKit uses this information to compute advanced lighting effects on the surface.

For a custom shader program, you use this semantic to bind SceneKit’s vertex tangent data to an input attribute of the shader.

Vertex tangent data is typically an array of three- or four-component vectors.

## See Also

- [static let color: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/color.md)
  The semantic for per-vertex color data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/tangent)*