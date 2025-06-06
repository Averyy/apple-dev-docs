# players(with:)

**Framework**: GameKit  
**Kind**: method

Retrieves a list of players with the specified connection state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func players(with state: GKConnectionState) -> [GKCloudPlayer]
```

#### Return Value

An array of players with the indicated connection state.

## Parameters

- `state`: A GKConnectionState used to find the requested players.

## See Also

- [func setConnectionState(GKConnectionState, completionHandler: ((any Error)?) -> Void)](gkgamesession/setconnectionstate(_:completionhandler:).md)
  Sets the connection state for the player.
- [func send(Data, with: GKTransportType, completionHandler: ((any Error)?) -> Void)](gkgamesession/send(_:with:completionhandler:).md)
  Sends the indicated data to all connected players.
- [enum GKTransportType](gktransporttype.md)
  The mechanism used to send messages to other players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/players(with:))*