# defaultInvitationMessage

**Framework**: GameKit  
**Kind**: property

The default invitation message sent to a player.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var defaultInvitationMessage: String? { get set }
```

#### Discussion

Your game sets this property to change the default invitation text displayed when the local player creates a new invitation. The local player may edit the text before sending the invitation.

## See Also

- [func setHostedPlayer(String, connected: Bool)](gkmatchmakerviewcontroller/sethostedplayer(_:connected:).md)
  Updates a player’s status on the view to show that the player has connected or disconnected from your server.
- [func setHostedPlayerReady(String)](gkmatchmakerviewcontroller/sethostedplayerready(_:).md)
  Informs the controller that a player has joined a hosted match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/defaultinvitationmessage)*