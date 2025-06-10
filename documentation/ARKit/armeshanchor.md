# ARMeshAnchor

**Framework**: ARKit  
**Kind**: class

An anchor for a physical object that ARKit detects and recreates virtually using a polygonal mesh.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class ARMeshAnchor
```

#### Overview

ARKit subdivides the reconstructed, real-world scene surrounding the user into mesh anchors.

Mesh anchors constantly update their data as ARKit refines its understanding of the real world. Although ARKit updates a mesh to reflect a change in the physical environment (such as when a person pulls out a chair), the mesh’s subsequent change is not intended to reflect in real time.

## Topics

### Accessing the Mesh
- [var geometry: ARMeshGeometry](armeshanchor/geometry.md)
  3D information about the mesh such as its shape and classifications.
- [class ARMeshGeometry](armeshgeometry.md)
  Mesh information stored in an efficient, array-based format.

## Relationships

### Inherits From
- [ARAnchor](aranchor.md)
### Conforms To
- [ARAnchorCopying](aranchorcopying.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking and visualizing planes](tracking-and-visualizing-planes.md)
  Detect surfaces in the physical environment and visualize their shape and location in 3D space.
- [class ARPlaneAnchor](arplaneanchor.md)
  An anchor for a 2D planar surface that ARKit detects in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshanchor)*