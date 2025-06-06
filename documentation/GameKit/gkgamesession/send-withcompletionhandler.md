# send(_:with:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sends the indicated data to all connected players.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func send(_ data: Data, with transport: GKTransportType) async throws
```

## Parameters

- `data`: A   object containing the information to be sent.
- `transport`: Determines how the data is sent.
- `completionHandler`: A block that is called after the data has been sent.

## See Also

- [func setConnectionState(GKConnectionState, completionHandler: ((any Error)?) -> Void)](gkgamesession/setconnectionstate(_:completionhandler:).md)
  Sets the connection state for the player.
- [func players(with: GKConnectionState) -> [GKCloudPlayer]](gkgamesession/players(with:).md)
  Retrieves a list of players with the specified connection state.
- [enum GKTransportType](gktransporttype.md)
  The mechanism used to send messages to other players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/send(_:with:completionhandler:))*