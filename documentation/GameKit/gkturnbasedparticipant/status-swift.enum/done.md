# GKTurnBasedParticipant.Status.done

**Framework**: GameKit  
**Kind**: case

The participant leaves the match.

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
case done
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

You set the [`matchOutcome`](gkturnbasedparticipant/matchoutcome.md) property to state the reason why the participant left.

## See Also

- [GKTurnBasedParticipant.Status.unknown](gkturnbasedparticipant/status-swift.enum/unknown.md)
  The participant is in an unexpected state.
- [GKTurnBasedParticipant.Status.invited](gkturnbasedparticipant/status-swift.enum/invited.md)
  The participant is invited to the match, but hasn’t responded to the invitation.
- [GKTurnBasedParticipant.Status.declined](gkturnbasedparticipant/status-swift.enum/declined.md)
  The participant declines the invitation to join the match, automatically terminating the match.
- [GKTurnBasedParticipant.Status.matching](gkturnbasedparticipant/status-swift.enum/matching.md)
  The participant represents an unfilled position in the match that Game Center promises to fill when needed.
- [GKTurnBasedParticipant.Status.active](gkturnbasedparticipant/status-swift.enum/active.md)
  The participant joins the match and is an active player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.enum/done)*