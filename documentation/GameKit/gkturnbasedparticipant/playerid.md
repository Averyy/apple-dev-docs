# playerID

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player identifier for this participant.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: User [`player`](./player.md) instead.

## Declaration

```swift
var playerID: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * playerID;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * playerID;
```

#### Discussion

This property is `nil` if this slot isn’t filled yet — for example, when Game Center uses automatch to fill this slot.

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
- [GKTurnBasedParticipant.Status](./status-swift.enum.md)
  The state the participant is in during the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/playerid)*