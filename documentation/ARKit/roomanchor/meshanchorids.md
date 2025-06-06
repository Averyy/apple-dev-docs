# meshAnchorIDs

**Framework**: ARKit  
**Kind**: property

An array of IDs of the mesh anchors associated with a room.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var meshAnchorIDs: [UUID] { get }
```

## See Also

- [var geometry: MeshAnchor.Geometry](roomanchor/geometry.md)
  The geometry of the mesh in an anchor’s coordinate system.
- [var id: UUID](roomanchor/id.md)
  The unique identifier of this anchor.
- [var isCurrentRoom: Bool](roomanchor/iscurrentroom.md)
  A Boolean value that indicates whether a room is a person’s current location.
- [var originFromAnchorTransform: simd_float4x4](roomanchor/originfromanchortransform.md)
  The transform from the room anchor to the origin coordinate system.
- [var planeAnchorIDs: [UUID]](roomanchor/planeanchorids.md)
  An array of IDs of the plane anchors associated with a room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/meshanchorids)*