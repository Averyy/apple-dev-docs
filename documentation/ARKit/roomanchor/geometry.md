# geometry

**Framework**: ARKit  
**Kind**: property

The geometry of the mesh in an anchor’s coordinate system.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var geometry: MeshAnchor.Geometry { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/geometry)*