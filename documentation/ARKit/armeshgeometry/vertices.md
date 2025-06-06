# vertices

**Framework**: ARKit  
**Kind**: property

The vertices of the mesh.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var vertices: ARGeometrySource { get }
```

#### Discussion

The [`count`](argeometrysource/count.md) equals the total number of vertices. Since each vertex is the type `SIMD3<Float>`, [`componentsPerVector`](argeometrysource/componentspervector.md) is three.

The following code demonstrates retrieving a vertex at a particular index.

```swift
extension ARMeshGeometry { 
    func vertex(at index: UInt32) -> SIMD3<Float> {
        assert(vertices.format == MTLVertexFormat.float3, "Expected three floats (twelve bytes) per vertex.")
        let vertexPointer = vertices.buffer.contents().advanced(by: vertices.offset + (vertices.stride * Int(index)))
        let vertex = vertexPointer.assumingMemoryBound(to: SIMD3<Float>.self).pointee
        return vertex
    }
}
```

## See Also

- [class ARGeometrySource](argeometrysource.md)
  Mesh data in a buffer-based array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshgeometry/vertices)*