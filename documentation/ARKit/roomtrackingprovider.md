# RoomTrackingProvider

**Framework**: ARKit  
**Kind**: class

A source of real-time information about the room that a person is currently in.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class RoomTrackingProvider
```

## Topics

### Creating a room-tracking provider
- [init()](roomtrackingprovider/init.md)
  Creates a room-tracking provider.
### Inspecting a room-tracking provider
- [var allAnchors: [RoomAnchor]](roomtrackingprovider/allanchors.md)
  An array of the room anchors the room-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<RoomAnchor>](roomtrackingprovider/anchorupdates.md)
  An asynchronous sequence of room anchor updates.
- [var currentRoomAnchor: RoomAnchor?](roomtrackingprovider/currentroomanchor.md)
  The room a person is in currently, if any.
- [var description: String](roomtrackingprovider/description.md)
  A textual representation of this room tracking provider.
- [var state: DataProviderState](roomtrackingprovider/state.md)
  The state of a room-tracking provider.
### Type properties
- [static var isSupported: Bool](roomtrackingprovider/issupported.md)
  A Boolean values that indicates whether a device supports the room-tracking provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](roomtrackingprovider/requiredauthorizations.md)
  An array of authorization types the room-tracking provider requires.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct RoomAnchor](roomanchor.md)
  The representation of a room ARKit is currently tracking.
- [enum SurfaceClassification](surfaceclassification.md)
  A value describing the classification of a surface.
- [Building local experiences with room tracking](../visionOS/building-local-experiences-with-room-tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomtrackingprovider)*