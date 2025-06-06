# setHostedPlayerReady(_:)

**Framework**: GameKit  
**Kind**: method

Informs the controller that a player has joined a hosted match.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setHostedPlayerReady(_ playerID: String)
```

#### Discussion

In a hosted match, when a new player connects to the server, your server needs to inform all participating devices connected to the match. Each participating device must separately call this method to update its matchmaking user interface.

## Parameters

- `playerID`: The identifier string for a player that connected to the external server.

## See Also

- [func setHostedPlayer(String, connected: Bool)](gkmatchmakerviewcontroller/sethostedplayer(_:connected:).md)
  Updates a player’s status on the view to show that the player has connected or disconnected from your server.
- [var defaultInvitationMessage: String?](gkmatchmakerviewcontroller/defaultinvitationmessage.md)
  The default invitation message sent to a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/sethostedplayerready(_:))*