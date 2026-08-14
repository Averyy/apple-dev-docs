# GKMeshGraphTriangulationMode

**Framework**: GameplayKit  
**Kind**: struct

Options for how to place graph nodes when generating the graph, used by the [`triangulationMode`](gkmeshgraph/triangulationmode.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GKMeshGraphTriangulationMode
```

## Topics

### Constants
- [static var vertices: GKMeshGraphTriangulationMode](gkmeshgraphtriangulationmode/vertices.md)
  An option to place graph nodes at each vertex in the generated mesh.
- [static var centers: GKMeshGraphTriangulationMode](gkmeshgraphtriangulationmode/centers.md)
  An option to place graph nodes at the center of each polygon in the generated mesh.
- [static var edgeMidpoints: GKMeshGraphTriangulationMode](gkmeshgraphtriangulationmode/edgemidpoints.md)
  An option to place graph nodes at the midpoint of each in the generated mesh.
### Initializers
- [init(rawValue: UInt)](gkmeshgraphtriangulationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [struct GKTriangle](gktriangle.md)
  The definition of a triangle in the mesh, available with the [`triangle(at:)`](gkmeshgraph/triangle(at:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode)*