# GKTurnBasedParticipant.Status.active

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The participant joins the match and is an active player.

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
case active
```

```c
GKTurnBasedParticipantStatusActive
```

## Mentions

- [Starting turn-based matches and passing turns between players](../../starting-turn-based-matches-and-passing-turns-between-players.md)

## See Also

### Constants
- [GKTurnBasedParticipant.Status.unknown](./unknown.md)
  The participant is in an unexpected state.
- [GKTurnBasedParticipant.Status.invited](./invited.md)
  The participant is invited to the match, but hasn’t responded to the invitation.
- [GKTurnBasedParticipant.Status.declined](./declined.md)
  The participant declines the invitation to join the match, automatically terminating the match.
- [GKTurnBasedParticipant.Status.matching](./matching.md)
  The participant represents an unfilled position in the match that Game Center promises to fill when needed.
- [GKTurnBasedParticipant.Status.done](./done.md)
  The participant leaves the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.enum/active)*