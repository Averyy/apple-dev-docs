# setHostedPlayer(_:connected:)

**Framework**: GameKit  
**Kind**: method

Updates a player’s status on the view to show that the player has connected or disconnected from your server.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setHostedPlayer(_ playerID: String, connected: Bool)
```

#### Discussion

When setting up a hosted match, each device needs to create a matchmaker view controller and display it to the player. Then, when a new player connects to your server, your server needs to notify all participating devices already connected to your server. Each participating device then calls this method to update that player’s status in the matchmaking interface. Similarly, if a player disconnects from the server, your server informs each device so the devices can update their user interface.

## Parameters

- `playerID`: The identifier string for a player that connected to the external server.
- `connected`: A Boolean value that states whether the player is connected to the hosted match.

## See Also

- [func setHostedPlayerReady(String)](gkmatchmakerviewcontroller/sethostedplayerready(_:).md)
  Informs the controller that a player has joined a hosted match.
- [var defaultInvitationMessage: String?](gkmatchmakerviewcontroller/defaultinvitationmessage.md)
  The default invitation message sent to a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/sethostedplayer(_:connected:))*