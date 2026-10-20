# player(_:didRequestMatchWithPlayers:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles the event when the local player sends other players an invitation to join a match.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`player(_:didRequestMatchWithRecipients:)`](./player%28_,didrequestmatchwithrecipients%29.md) method instead.

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String])
```

```objc
- (void) player:(GKPlayer *) player didRequestMatchWithPlayers:(NSArray<NSString *> *) playerIDsToInvite;
```

#### Discussion

When you call this method, GameKit launches the game and starts the matchmaking process.

## Parameters

- `player`: The local player who sends the invitation.
- `playerIDsToInvite`: The identifiers for the players who receive invitations to join the match.

## See Also

### Starting a New Match
- [func player(GKPlayer, didAccept: GKInvite)](./player%28_,didaccept%29.md)
  Handles the event when the local player accepts an invitation from another player.
- [func player(GKPlayer, didRequestMatchWithRecipients: [GKPlayer])](./player%28_,didrequestmatchwithrecipients%29.md)
  Handles the event when the local player sends other players an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/player(_:didrequestmatchwithplayers:))*