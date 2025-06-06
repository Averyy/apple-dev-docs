# playerID

**Framework**: GameKit  
**Kind**: property

The player identifier for this participant.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var playerID: String? { get }
```

#### Discussion

This property is `nil` if this slot isn’t filled yet — for example, when Game Center uses automatch to fill this slot.

## See Also

- [var lastTurnDate: Date?](gkturnbasedparticipant/lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var timeoutDate: Date?](gkturnbasedparticipant/timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](gkturnbasedparticipant/player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](gkturnbasedparticipant/status-swift.enum.md)
  The state the participant is in during the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/playerid)*