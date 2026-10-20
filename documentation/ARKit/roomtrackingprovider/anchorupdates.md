# anchorUpdates

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of room anchor updates.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var anchorUpdates: AnchorUpdateSequence<RoomAnchor> { get }
```

## See Also

### Inspecting a room-tracking provider
- [var allAnchors: [RoomAnchor]](./allanchors.md)
  An array of the room anchors the room-tracking provider is tracking.
- [var currentRoomAnchor: RoomAnchor?](./currentroomanchor.md)
  The room a person is in currently, if any.
- [var description: String](./description.md)
  A textual representation of this room tracking provider.
- [var state: DataProviderState](./state.md)
  The state of a room-tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomtrackingprovider/anchorupdates)*