# edgeCrease

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The semantic for edge crease data, used for subdividing surfaces.

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
static let edgeCrease: SCNGeometrySource.Semantic
```

```c
extern SCNGeometrySourceSemantic const SCNGeometrySourceSemanticEdgeCrease;
```

## Discussion

For a geometry source, this semantic identifies data containing crease data for each vertex in the geometry. SceneKit uses this information to determine the sharpness of edges and smoothness of surfaces when you change a geometry’s [`subdivisionLevel`](../../scngeometry/subdivisionlevel.md) property.

For a custom shader program, you use this semantic to bind SceneKit’s edge crease data to an input attribute of the shader.

Edge crease data is an array of scalar floating-point values, where each value determines the smoothness or sharpness of the edge identified by the primitive at the corresponding index in the geometry’s [SceneKit Constants](../../scenekit-constants.md) geometry element: A value of `0.0` specifies a completely smoothed edge, and a value of `10.0` or greater specifies an infinitely sharp edge.

## See Also

### Surface Subdivision Semantics
- [static let vertexCrease: SCNGeometrySource.Semantic](./vertexcrease.md)
  The semantic for vertex crease data, used for subdividing surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct/edgecrease)*