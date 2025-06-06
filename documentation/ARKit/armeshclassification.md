# ARMeshClassification

**Framework**: ARKit  
**Kind**: enum

Enumeration of different classes of real-world objects that ARKit can identify.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
enum ARMeshClassification
```

#### Overview

When you enable [`sceneReconstruction`](arworldtrackingconfiguration/scenereconstruction.md) on a world-tracking configuration, ARKit provides several mesh anchors ([`ARMeshAnchor`](armeshanchor.md)) that collectively estimate the shape of the physical environment. Within that model of the real world, ARKit may identify specific objects, like seats, windows, tables, or walls. ARKit shares that information by exposing one or more [`ARMeshClassification`](armeshclassification.md) instances in a mesh’s [`geometry`](armeshanchor/geometry.md) property.

For a sample app that demonstrates mesh classification, see [`Visualizing and interacting with a reconstructed scene`](visualizing-and-interacting-with-a-reconstructed-scene.md).

## Topics

### Options
- [ARMeshClassification.ceiling](armeshclassification/ceiling.md)
  The face is a part of a real-world ceiling.
- [ARMeshClassification.door](armeshclassification/door.md)
  The face is a part of a real-world door.
- [ARMeshClassification.floor](armeshclassification/floor.md)
  The face is a part of a real-world floor.
- [ARMeshClassification.none](armeshclassification/none.md)
  A face ARKit can’t classify.
- [ARMeshClassification.seat](armeshclassification/seat.md)
  The face is a part of a real-world seat.
- [ARMeshClassification.table](armeshclassification/table.md)
  The face is a part of a real-world table.
- [ARMeshClassification.wall](armeshclassification/wall.md)
  The face is a part of a real-world wall.
- [ARMeshClassification.window](armeshclassification/window.md)
  The face is a part of a real-world window.
### Initializers
- [init?(rawValue: Int)](armeshclassification/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var classification: ARGeometrySource?](armeshgeometry/classification.md)
  Classification for each face in the mesh.
- [var faces: ARGeometryElement](armeshgeometry/faces.md)
  An object that contains a buffer of vertex indices of the geometry’s faces.
- [class ARGeometryElement](argeometryelement.md)
  A container for index data, such as vertex indices of a face.
- [var normals: ARGeometrySource](armeshgeometry/normals.md)
  Rays that define which direction is outside for each face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshclassification)*