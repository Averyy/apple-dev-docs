# player(_:didRequestMatchWithRecipients:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles the event when the local player sends other players an invitation to join a match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithRecipients recipientPlayers: [GKPlayer])
```

```objc
- (void) player:(GKPlayer *) player didRequestMatchWithRecipients:(NSArray<GKPlayer *> *) recipientPlayers;
```

## Discussion

When GameKit calls this method, Game Center starts the matchmaking process.

## Parameters

- `player`: The local player who sends the invitation.
- `recipientPlayers`: The players who receive invitations to join the match.

## See Also

### Starting a New Match
- [func player(GKPlayer, didAccept: GKInvite)](./player%28_,didaccept%29.md)
  Handles the event when the local player accepts an invitation from another player.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](./player%28_,didrequestmatchwithplayers%29.md)
  Handles the event when the local player sends other players an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/player(_:didrequestmatchwithrecipients:))*