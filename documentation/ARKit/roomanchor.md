# RoomAnchor

**Framework**: ARKit  
**Kind**: struct

The representation of a room ARKit is currently tracking.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct RoomAnchor
```

#### Overview

A `RoomAnchor` structure describes an approximate representation of the room’s geometry, and contains arrays with identifiers of mesh and plane anchors that the framework associates with that room.

## Topics

### Getting information about a room anchor
- [var geometry: MeshAnchor.Geometry](roomanchor/geometry.md)
  The geometry of the mesh in an anchor’s coordinate system.
- [var id: UUID](roomanchor/id.md)
  The unique identifier of this anchor.
- [var isCurrentRoom: Bool](roomanchor/iscurrentroom.md)
  A Boolean value that indicates whether a room is a person’s current location.
- [var meshAnchorIDs: [UUID]](roomanchor/meshanchorids.md)
  An array of IDs of the mesh anchors associated with a room.
- [var originFromAnchorTransform: simd_float4x4](roomanchor/originfromanchortransform.md)
  The transform from the room anchor to the origin coordinate system.
- [var planeAnchorIDs: [UUID]](roomanchor/planeanchorids.md)
  An array of IDs of the plane anchors associated with a room.
### Inspecting a room anchor
- [func contains(SIMD3<Float>) -> Bool](roomanchor/contains(_:).md)
  Returns a Boolean value that indicates whether a room contains the provided point.
- [func geometries(of: MeshAnchor.MeshClassification) -> [MeshAnchor.Geometry]](roomanchor/geometries(of:).md)
  Returns the disjoint mesh geometries of a given classification.
- [var description: String](roomanchor/description.md)
  A textual representation of this anchor.
### Operators
- [static func == (RoomAnchor, RoomAnchor) -> Bool](roomanchor/==(_:_:).md)
  Returns a Boolean value indicating whether two room anchors are equal.
### Instance Methods
- [func geometries(classifiedAs: SurfaceClassification) -> [MeshAnchor.Geometry]](roomanchor/geometries(classifiedas:).md)
  Get disjoint mesh geometries of a given surface classification.
### Default Implementations
- [ARKitCoordinateSpaceProviding Implementations](roomanchor/arkitcoordinatespaceproviding-implementations.md)

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](arkitcoordinatespaceproviding.md)
- [Anchor](anchor.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class RoomTrackingProvider](roomtrackingprovider.md)
  A source of real-time information about the room that a person is currently in.
- [enum SurfaceClassification](surfaceclassification.md)
  A value describing the classification of a surface.
- [Building local experiences with room tracking](../visionos/building-local-experiences-with-room-tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor)*