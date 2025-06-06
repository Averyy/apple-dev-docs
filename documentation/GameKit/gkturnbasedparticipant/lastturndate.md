# lastTurnDate

**Framework**: GameKit  
**Kind**: property

The date and time that this participant last took a turn in the game.

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
var lastTurnDate: Date? { get }
```

#### Discussion

This property is invalid until the participant takes their first turn.

## See Also

- [var timeoutDate: Date?](gkturnbasedparticipant/timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](gkturnbasedparticipant/player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](gkturnbasedparticipant/playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/lastturndate)*