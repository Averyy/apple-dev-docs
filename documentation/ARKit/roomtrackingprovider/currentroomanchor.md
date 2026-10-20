# currentRoomAnchor

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The room a person is in currently, if any.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var currentRoomAnchor: RoomAnchor? { get }
```

## See Also

### Inspecting a room-tracking provider
- [var allAnchors: [RoomAnchor]](./allanchors.md)
  An array of the room anchors the room-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<RoomAnchor>](./anchorupdates.md)
  An asynchronous sequence of room anchor updates.
- [var description: String](./description.md)
  A textual representation of this room tracking provider.
- [var state: DataProviderState](./state.md)
  The state of a room-tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomtrackingprovider/currentroomanchor)*