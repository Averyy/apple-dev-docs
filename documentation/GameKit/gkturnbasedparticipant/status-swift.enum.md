# GKTurnBasedParticipant.Status

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GKTurnBasedParticipantStatus : NSInteger;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Topics

### Constants
- [GKTurnBasedParticipant.Status.unknown](./status-swift.enum/unknown.md)
  The participant is in an unexpected state.
- [GKTurnBasedParticipant.Status.invited](./status-swift.enum/invited.md)
  The participant is invited to the match, but hasn’t responded to the invitation.
- [GKTurnBasedParticipant.Status.declined](./status-swift.enum/declined.md)
  The participant declines the invitation to join the match, automatically terminating the match.
- [GKTurnBasedParticipant.Status.matching](./status-swift.enum/matching.md)
  The participant represents an unfilled position in the match that Game Center promises to fill when needed.
- [GKTurnBasedParticipant.Status.active](./status-swift.enum/active.md)
  The participant joins the match and is an active player.
- [GKTurnBasedParticipant.Status.done](./status-swift.enum/done.md)
  The participant leaves the match.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving Participant Details
- [var lastTurnDate: Date?](./lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var timeoutDate: Date?](./timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](./player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](./status-swift.property.md)
  The status of the participant.
- [var playerID: String?](./playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.enum)*