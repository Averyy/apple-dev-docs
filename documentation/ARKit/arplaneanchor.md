# ARPlaneAnchor

**Framework**: ARKit  
**Kind**: class

An anchor for a 2D planar surface that ARKit detects in the physical environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARPlaneAnchor
```

#### Overview

When you enable [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) in a world tracking session, ARKit notifies your app of all the surfaces it observes using the device’s back camera. ARKit calls your delegate’s [`session(_:didAdd:)`](arsessiondelegate/session(_:didadd:).md) with an [`ARPlaneAnchor`](arplaneanchor.md) for each unique surface. Each plane anchor provides details about the surface, like its real-world position and shape.

The width and length of a plane (the [`planeExtent`](arplaneanchor/planeextent.md)) span the xz-plane of an [`ARPlaneAnchor`](arplaneanchor.md) instance’s local coordinate system. The y-axis of the plane anchor is the plane’s normal vector.

## Topics

### Orientation
- [var alignment: ARPlaneAnchor.Alignment](arplaneanchor/alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [ARPlaneAnchor.Alignment](arplaneanchor/alignment-swift.enum.md)
  The kinds of alignment — horizontal or vertical — that a plane anchor can have.
### Geometry
- [var geometry: ARPlaneGeometry](arplaneanchor/geometry.md)
  A coarse triangle mesh representing the general shape of the detected plane.
- [class ARPlaneGeometry](arplanegeometry.md)
  A 3D mesh describing the shape of a detected plane in world-tracking AR sessions.
- [class ARSCNPlaneGeometry](arscnplanegeometry.md)
  A SceneKit representation of the 2D shape of a plane, for use with plane detection results in an AR session.
### Dimensions
- [var center: simd_float3](arplaneanchor/center.md)
  The center point of the plane relative to its anchor position.
- [var planeExtent: ARPlaneExtent](arplaneanchor/planeextent.md)
  The estimated width, length, and y-axis rotation of the detected plane.
- [class ARPlaneExtent](arplaneextent.md)
  The size and y-axis rotation of a detected plane.
- [var extent: simd_float3](arplaneanchor/extent.md)
  The estimated width and length of the detected plane.
### Classifying a Plane
- [class var isClassificationSupported: Bool](arplaneanchor/isclassificationsupported.md)
  A Boolean value that indicates whether plane classification is available on the current device.
- [var classification: ARPlaneAnchor.Classification](arplaneanchor/classification-2r4x8.md)
  A general characterization of what kind of real-world surface the plane anchor represents.
- [ARPlaneAnchor.Classification](arplaneanchor/classification-swift.enum.md)
  Possible characterizations of real-world surfaces represented by plane anchors.

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

## See Also

- [Tracking and visualizing planes](tracking-and-visualizing-planes.md)
  Detect surfaces in the physical environment and visualize their shape and location in 3D space.
- [class ARMeshAnchor](armeshanchor.md)
  An anchor for a physical object that ARKit detects and recreates virtually using a polygonal mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor)*