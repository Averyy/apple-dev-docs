# timeoutDate

**Framework**: GameKit  
**Kind**: property

The date and time that the participant’s turn timed out.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var timeoutDate: Date? { get }
```

#### Discussion

This property is `nil` when the participant takes a turn that doesn’t time out.

## See Also

- [var lastTurnDate: Date?](gkturnbasedparticipant/lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var player: GKPlayer?](gkturnbasedparticipant/player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](gkturnbasedparticipant/playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/timeoutdate)*