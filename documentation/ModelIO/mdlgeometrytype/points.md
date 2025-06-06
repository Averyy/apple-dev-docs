# MDLGeometryType.points

**Framework**: Model I/O  
**Kind**: case

Each index in the submesh refers to a vertex to be rendered as a single point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case points
```

## See Also

- [MDLGeometryType.lines](mdlgeometrytype/lines.md)
  Each pair of consecutive indices in the submesh refers to two vertices to be rendered as a line segment.
- [MDLGeometryType.triangles](mdlgeometrytype/triangles.md)
  Each set of three consecutive indices in the submesh refers to three vertices to be rendered as a triangle.
- [MDLGeometryType.triangleStrips](mdlgeometrytype/trianglestrips.md)
  The first three consecutive indices in the submesh refer to three vertices to be rendered as a triangle. Each subsequent index refers to another vertex that completes a triangle formed by connecting it to the previous two vertices.
- [MDLGeometryType.quads](mdlgeometrytype/quads.md)
  Each set of four consecutive indices in the submesh refers to four vertices to be rendered as a quadrilateral.
- [MDLGeometryType.variableTopology](mdlgeometrytype/variabletopology.md)
  The submesh’s index buffer does not contain a uniform set of primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlgeometrytype/points)*