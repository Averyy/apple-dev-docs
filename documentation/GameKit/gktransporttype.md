# GKTransportType

**Framework**: GameKit  
**Kind**: enum

The mechanism used to send messages to other players in a game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKTransportType
```

## Topics

### Constants
- [GKTransportType.reliable](gktransporttype/reliable.md)
  The data is sent continuously until it is successfully received by the intended recipients or the connection times out.
- [GKTransportType.unreliable](gktransporttype/unreliable.md)
  The data is sent once and is not sent again if a transmission error occurs.
### Initializers
- [init?(rawValue: Int)](gktransporttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setConnectionState(GKConnectionState, completionHandler: ((any Error)?) -> Void)](gkgamesession/setconnectionstate(_:completionhandler:).md)
  Sets the connection state for the player.
- [func players(with: GKConnectionState) -> [GKCloudPlayer]](gkgamesession/players(with:).md)
  Retrieves a list of players with the specified connection state.
- [func send(Data, with: GKTransportType, completionHandler: ((any Error)?) -> Void)](gkgamesession/send(_:with:completionhandler:).md)
  Sends the indicated data to all connected players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gktransporttype)*