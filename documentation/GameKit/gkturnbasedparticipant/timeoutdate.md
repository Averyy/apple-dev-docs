# timeoutDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * timeoutDate;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * timeoutDate;
```

## Discussion

This property is `nil` when the participant takes a turn that doesn’t time out.

## See Also

### Retrieving Participant Details
- [var lastTurnDate: Date?](./lastturndate.md)
  The date and time that this participant last took a turn in the game.
- [var player: GKPlayer?](./player.md)
  The player object containing the participant details.
- [var status: GKTurnBasedParticipant.Status](./status-swift.property.md)
  The status of the participant.
- [GKTurnBasedParticipant.Status](./status-swift.enum.md)
  The state the participant is in during the match.
- [var playerID: String?](./playerid.md)
  The player identifier for this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/timeoutdate)*