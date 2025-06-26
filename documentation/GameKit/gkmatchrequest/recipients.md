# recipients

**Framework**: GameKit  
**Kind**: property

The players to invite to the match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var recipients: [GKPlayer]? { get set }
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)

#### Discussion

If this property is non-`nil`, GameKit invites the specified players. GameKit doesn’t use automatch to fill player slots, and ignores the [`maxPlayers`](gkmatchrequest/maxplayers.md) and [`minPlayers`](gkmatchrequest/minplayers.md) properties. The default value is `nil`.

## See Also

- [var inviteMessage: String?](gkmatchrequest/invitemessage.md)
  The message sent to other players when the local player invites them to join a match.
- [var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)?](gkmatchrequest/recipientresponsehandler.md)
  A method that handles when a player responds to an invitation to join a match.
- [enum GKInviteRecipientResponse](gkinviterecipientresponse.md)
  A player’s response to an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/recipients)*