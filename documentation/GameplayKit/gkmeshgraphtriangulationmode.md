# GKMeshGraphTriangulationMode

**Framework**: GameplayKit  
**Kind**: struct  
**Role**: Structure

Options for how to place graph nodes when generating the graph, used by the [`triangulationMode`](./gkmeshgraph/triangulationmode.md) property.

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

```c
enum GKMeshGraphTriangulationMode : NSUInteger;
```

## Topics

### Constants
- [static var vertices: GKMeshGraphTriangulationMode](./gkmeshgraphtriangulationmode/vertices.md)
  An option to place graph nodes at each vertex in the generated mesh.
- [static var centers: GKMeshGraphTriangulationMode](./gkmeshgraphtriangulationmode/centers.md)
  An option to place graph nodes at the center of each polygon in the generated mesh.
- [static var edgeMidpoints: GKMeshGraphTriangulationMode](./gkmeshgraphtriangulationmode/edgemidpoints.md)
  An option to place graph nodes at the midpoint of each in the generated mesh.
### Initializers
- [init(rawValue: UInt)](./gkmeshgraphtriangulationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [struct GKTriangle](./gktriangle.md)
  The definition of a triangle in the mesh, available with the [`triangle(at:)`](./gkmeshgraph/triangle%28at%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode)*