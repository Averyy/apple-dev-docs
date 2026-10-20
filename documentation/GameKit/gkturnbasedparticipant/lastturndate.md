# lastTurnDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * lastTurnDate;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * lastTurnDate;
```

#### Discussion

This property is invalid until the participant takes their first turn.

## See Also

### Retrieving Participant Details
- [var timeoutDate: Date?](./timeoutdate.md)
  The date and time that the participant’s turn timed out.
- [var player: GKPlayer?](./player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](./status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](./status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](./playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/lastturndate)*