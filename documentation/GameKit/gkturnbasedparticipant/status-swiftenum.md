# GKTurnBasedParticipant.Status

**Framework**: GameKit  
**Kind**: enum

The state the participant is in during the match.

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
enum Status
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

## Topics

### Constants
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
- [GKTurnBasedParticipant.Status.done](gkturnbasedparticipant/status-swift.enum/done.md)
  The participant leaves the match.
### Initializers
- [init?(rawValue: Int)](gkturnbasedparticipant/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var lastTurnDate: Date?](gkturnbasedparticipant/lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var timeoutDate: Date?](gkturnbasedparticipant/timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](gkturnbasedparticipant/player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.property.md)
  The status of the participant.
- [var playerID: String?](gkturnbasedparticipant/playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.enum)*