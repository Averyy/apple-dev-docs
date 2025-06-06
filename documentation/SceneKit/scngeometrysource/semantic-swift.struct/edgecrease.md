# edgeCrease

**Framework**: SceneKit  
**Kind**: property

The semantic for edge crease data, used for subdividing surfaces.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let edgeCrease: SCNGeometrySource.Semantic
```

#### Discussion

For a geometry source, this semantic identifies data containing crease data for each vertex in the geometry. SceneKit uses this information to determine the sharpness of edges and smoothness of surfaces when you change a geometry’s [`subdivisionLevel`](scngeometry/subdivisionlevel.md) property.

For a custom shader program, you use this semantic to bind SceneKit’s edge crease data to an input attribute of the shader.

Edge crease data is an array of scalar floating-point values, where each value determines the smoothness or sharpness of the edge identified by the primitive at the corresponding index in the geometry’s [`SceneKit Constants`](scenekit-constants.md) geometry element: A value of `0.0` specifies a completely smoothed edge, and a value of `10.0` or greater specifies an infinitely sharp edge.

## See Also

- [static let vertexCrease: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/vertexcrease.md)
  The semantic for vertex crease data, used for subdividing surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/edgecrease)*