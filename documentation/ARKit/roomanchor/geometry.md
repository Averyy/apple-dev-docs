# geometry

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The geometry of the mesh in an anchor’s coordinate system.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var geometry: MeshAnchor.Geometry { get }
```

## See Also

### Getting information about a room anchor
- [var id: UUID](./id.md)
  The unique identifier of this anchor.
- [var isCurrentRoom: Bool](./iscurrentroom.md)
  A Boolean value that indicates whether a room is a person’s current location.
- [var meshAnchorIDs: [UUID]](./meshanchorids.md)
  An array of IDs of the mesh anchors associated with a room.
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the room anchor to the origin coordinate system.
- [var planeAnchorIDs: [UUID]](./planeanchorids.md)
  An array of IDs of the plane anchors associated with a room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/geometry)*