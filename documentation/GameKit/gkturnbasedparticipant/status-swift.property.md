# status

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The status of the participant.

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
var status: GKTurnBasedParticipant.Status { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) GKTurnBasedParticipantStatus status;
```

*macOS*

```objc
@property (atomic, readonly) GKTurnBasedParticipantStatus status;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## See Also

### Retrieving Participant Details
- [var lastTurnDate: Date?](./lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var timeoutDate: Date?](./timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](./player.md)
  The player object containing the participant details.
- [GKTurnBasedParticipant.Status](./status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](./playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/status-swift.property)*