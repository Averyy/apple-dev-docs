# players(with:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a list of players with the specified connection state.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
func players(with state: GKConnectionState) -> [GKCloudPlayer]
```

```objc
- (NSArray<GKCloudPlayer *> *) playersWithConnectionState:(GKConnectionState) state;
```

## Return Value

An array of players with the indicated connection state.

## Parameters

- `state`: A GKConnectionState used to find the requested players.

## See Also

### Connecting Players for Real-Time Communication
- [func setConnectionState(GKConnectionState, completionHandler: ((any Error)?) -> Void)](./setconnectionstate%28_,completionhandler%29.md)
  Sets the connection state for the player.
- [func send(Data, with: GKTransportType, completionHandler: ((any Error)?) -> Void)](./send%28_,with,completionhandler%29.md)
  Sends the indicated data to all connected players.
- [enum GKTransportType](../gktransporttype.md)
  The mechanism used to send messages to other players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/players(with:))*