# triangleCount

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The number of triangles in the mesh.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var triangleCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger triangleCount;
```

#### Discussion

This property’s value is valid only after calling the [`triangulate()`](./triangulate%28%29.md) to create a mesh around the current configuration of obstacles.

## See Also

### Managing the Mesh
- [func triangulate()](./triangulate%28%29.md)
  Creates or updates the graph with a network of nodes that describes the open space around its obstacles.
- [var triangulationMode: GKMeshGraphTriangulationMode](./triangulationmode.md)
  A set of options for how to place graph nodes when triangulating the graph.
- [func triangle(at: Int) -> GKTriangle](./triangle%28at%29.md)
  The triangle definition at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/trianglecount)*