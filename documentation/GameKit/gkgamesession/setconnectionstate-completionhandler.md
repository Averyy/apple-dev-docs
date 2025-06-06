# setConnectionState(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sets the connection state for the player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setConnectionState(_ state: GKConnectionState) async throws
```

#### Discussion

This method will fail when the game session’s player limit has already been reached or there are network problems. The game session’s `lastModifiedDate` and `lastModifiedPlayer` properties are updated on completion.

## Parameters

- `state`: The   to be assigned to the player.
- `completionHandler`: A block that is called after the connect state has been set.

## See Also

- [func players(with: GKConnectionState) -> [GKCloudPlayer]](gkgamesession/players(with:).md)
  Retrieves a list of players with the specified connection state.
- [func send(Data, with: GKTransportType, completionHandler: ((any Error)?) -> Void)](gkgamesession/send(_:with:completionhandler:).md)
  Sends the indicated data to all connected players.
- [enum GKTransportType](gktransporttype.md)
  The mechanism used to send messages to other players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/setconnectionstate(_:completionhandler:))*