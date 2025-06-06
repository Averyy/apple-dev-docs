# GKTurnBasedParticipant.Status.matching

**Framework**: GameKit  
**Kind**: case

The participant represents an unfilled position in the match that Game Center promises to fill when needed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case matching
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

When you make this participant the next person to take a turn in the match, Game Center fills the position and updates the [`status`](gkturnbasedparticipant/status-swift.property.md) and [`playerID`](gkturnbasedparticipant/playerid.md) properties.

## See Also

- [GKTurnBasedParticipant.Status.unknown](gkturnbasedparticipant/status-swift.enum/unknown.md)
  The participant is in an unexpected state.
- [GKTurnBasedParticipant.Status.invited](gkturnbasedparticipant/status-swift.enum/invited.md)
  The participant is invited to the match, but hasn’t responded to the invitation.
- [GKTurnBasedParticipant.Status.declined](gkturnbasedparticipant/status-swift.enum/declined.md)
  The participant declines the invitation to join the match, automatically terminating the match.
- [GKTurnBasedParticipant.Status.active](gkturnbasedparticipant/status-swift.enum/active.md)
  The participant joins the match and is an active player.
- [GKTurnBasedParticipant.Status.done](gkturnbasedparticipant/status-swift.enum/done.md)
  The participant leaves the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.enum/matching)*