# setHostedPlayerReady(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Informs the controller that a player has joined a hosted match.

**Availability**:
- iOS 4.1+ - Deprecated in 5.0
- iPadOS 4.1+ - Deprecated in 5.0
- Mac Catalyst 4.1+ - Deprecated in 5.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`setHostedPlayer(_:connected:)`](./sethostedplayer%28_,connected%29.md) method instead.

## Declaration

```swift
func setHostedPlayerReady(_ playerID: String)
```

```objc
- (void) setHostedPlayerReady:(NSString *) playerID;
```

## Discussion

In a hosted match, when a new player connects to the server, your server needs to inform all participating devices connected to the match. Each participating device must separately call this method to update its matchmaking user interface.

## Parameters

- `playerID`: The identifier string for a player that connected to the external server.

## See Also

### Deprecated
- [func setHostedPlayer(String, connected: Bool)](./sethostedplayer%28_,connected%29.md)
  Updates a player’s status on the view to show that the player has connected or disconnected from your server.
- [var defaultInvitationMessage: String?](./defaultinvitationmessage.md)
  The default invitation message sent to a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/sethostedplayerready(_:))*