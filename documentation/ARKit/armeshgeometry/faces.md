# faces

**Framework**: ARKit  
**Kind**: property

An object that contains a buffer of vertex indices of the geometry’s faces.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var faces: ARGeometryElement { get }
```

#### Discussion

Each element of the buffer-based array is a three-index combination that forms a unique triangle, or . The index refers to that vertex’s position in the [`vertices`](armeshgeometry/vertices.md) array. The [`count`](argeometryelement/count.md) of this property represents the number of faces.

The following code demonstrates getting the vertices of a particular face:

```swift
extension ARMeshGeometry {
    func vertexIndicesOf(faceWithIndex index: Int) -> [Int] {
        let indicesPerFace = faces.indexCountPerPrimitive
        let facesPointer = faces.buffer.contents()
        var vertexIndices = [Int]()
        for offset in 0..<indicesPerFace {
            let vertexIndexAddress = facesPointer.advanced(by: (index * indicesPerFace + offset) * MemoryLayout<UInt32>.size)
            vertexIndices.append(Int(vertexIndexAddress.assumingMemoryBound(to: UInt32.self).pointee))
        }
        return vertexIndices
    }
}
```

## See Also

- [var classification: ARGeometrySource?](armeshgeometry/classification.md)
  Classification for each face in the mesh.
- [enum ARMeshClassification](armeshclassification.md)
  Enumeration of different classes of real-world objects that ARKit can identify.
- [class ARGeometryElement](argeometryelement.md)
  A container for index data, such as vertex indices of a face.
- [var normals: ARGeometrySource](armeshgeometry/normals.md)
  Rays that define which direction is outside for each face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshgeometry/faces)*