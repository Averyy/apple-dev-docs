# defaultInvitationMessage

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The default invitation message sent to a player.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`inviteMessage`](../gkmatchrequest/invitemessage.md) property instead.

## Declaration

```swift
var defaultInvitationMessage: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * defaultInvitationMessage;
```

#### Discussion

Your game sets this property to change the default invitation text displayed when the local player creates a new invitation. The local player may edit the text before sending the invitation.

## See Also

### Deprecated
- [func setHostedPlayer(String, connected: Bool)](./sethostedplayer%28_,connected%29.md)
  Updates a player’s status on the view to show that the player has connected or disconnected from your server.
- [func setHostedPlayerReady(String)](./sethostedplayerready%28_%29.md)
  Informs the controller that a player has joined a hosted match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/defaultinvitationmessage)*