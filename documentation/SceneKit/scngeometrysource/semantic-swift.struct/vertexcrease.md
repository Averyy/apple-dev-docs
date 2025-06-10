# vertexCrease

**Framework**: SceneKit  
**Kind**: property

The semantic for vertex crease data, used for subdividing surfaces.

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
static let vertexCrease: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing crease data for each vertex in the geometry. SceneKit uses this information to determine the sharpness of corners and smoothness of surfaces when you change a geometry’s [`subdivisionLevel`](scngeometry/subdivisionlevel.md) property.

For a custom shader program, you use this semantic to bind SceneKit’s vertex crease data to an input attribute of the shader.

Vertex crease data is an array of scalar floating-point values, where each value determines the smoothness or sharpness of the corresponding vertex: A value of `0.0` specifies a completely smoothed corner, and a value of `10.0` or greater specifies an infinitely sharp point.

## See Also

- [static let edgeCrease: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/edgecrease.md)
  The semantic for edge crease data, used for subdividing surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/vertexcrease)*