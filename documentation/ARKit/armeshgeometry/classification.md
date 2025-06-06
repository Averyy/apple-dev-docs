# classification

**Framework**: ARKit  
**Kind**: property

Classification for each face in the mesh.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var classification: ARGeometrySource? { get }
```

#### Discussion

Each element of the array ([`ARGeometrySource`](argeometrysource.md)) is a classification that corresponds to one face in the geometry. The `count` of this property represents the number of faces in the geometry. The default value at each index is `0`, –– the raw value for [`ARMeshClassification.none`](armeshclassification/none.md).

The following code demonstrates retrieving a classification for a particular face:

```swift
extension ARMeshGeometry {
    func classificationOf(faceWithIndex index: Int) -> ARMeshClassification {
        guard let classification = classification else { return .none }
        let classificationAddress = classification.buffer.contents().advanced(by: index)
        let classificationValue = Int(classificationAddress.assumingMemoryBound(to: UInt8.self).pointee)
        return ARMeshClassification(rawValue: classificationValue) ?? .none
    }
}
```

For a sample app that demonstrates classification, see [`Visualizing and interacting with a reconstructed scene`](visualizing-and-interacting-with-a-reconstructed-scene.md).

## See Also

- [enum ARMeshClassification](armeshclassification.md)
  Enumeration of different classes of real-world objects that ARKit can identify.
- [var faces: ARGeometryElement](armeshgeometry/faces.md)
  An object that contains a buffer of vertex indices of the geometry’s faces.
- [class ARGeometryElement](argeometryelement.md)
  A container for index data, such as vertex indices of a face.
- [var normals: ARGeometrySource](armeshgeometry/normals.md)
  Rays that define which direction is outside for each face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshgeometry/classification)*