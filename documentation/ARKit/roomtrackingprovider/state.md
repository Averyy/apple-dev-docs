# state

**Framework**: ARKit  
**Kind**: property

The state of a room-tracking provider.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var state: DataProviderState { get }
```

## See Also

- [var allAnchors: [RoomAnchor]](roomtrackingprovider/allanchors.md)
  An array of the room anchors the room-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<RoomAnchor>](roomtrackingprovider/anchorupdates.md)
  An asynchronous sequence of room anchor updates.
- [var currentRoomAnchor: RoomAnchor?](roomtrackingprovider/currentroomanchor.md)
  The room a person is in currently, if any.
- [var description: String](roomtrackingprovider/description.md)
  A textual representation of this room tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomtrackingprovider/state)*