# MDLGeometryType.variableTopology

**Framework**: Model I/O  
**Kind**: case  
**Role**: Case

The submesh’s index buffer does not contain a uniform set of primitives.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case variableTopology
```

```c
MDLGeometryTypeVariableTopology
```

## Discussion

If a submesh has non-uniform topology, its [`topology`](../mdlsubmesh/topology.md) property contains an object describing how the arrangement of values in the index buffer combine to produce the submesh’s shape.

## See Also

### Constants
- [MDLGeometryType.points](./points.md)
  Each index in the submesh refers to a vertex to be rendered as a single point.
- [MDLGeometryType.lines](./lines.md)
  Each pair of consecutive indices in the submesh refers to two vertices to be rendered as a line segment.
- [MDLGeometryType.triangles](./triangles.md)
  Each set of three consecutive indices in the submesh refers to three vertices to be rendered as a triangle.
- [MDLGeometryType.triangleStrips](./trianglestrips.md)
  The first three consecutive indices in the submesh refer to three vertices to be rendered as a triangle. Each subsequent index refers to another vertex that completes a triangle formed by connecting it to the previous two vertices.
- [MDLGeometryType.quads](./quads.md)
  Each set of four consecutive indices in the submesh refers to four vertices to be rendered as a quadrilateral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlgeometrytype/variabletopology)*