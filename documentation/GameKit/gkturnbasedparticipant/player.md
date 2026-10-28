# player

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player object containing the participant details.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var player: GKPlayer? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) GKPlayer * player;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) GKPlayer * player;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

This property is `nil` if this slot isn’t filled yet — for example, when Game Center uses automatch to fill this slot.

## See Also

### Retrieving Participant Details
- [var lastTurnDate: Date?](./lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var timeoutDate: Date?](./timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var status: GKTurnBasedParticipant.Status](./status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](./status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](./playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/player)*