# matchOutcome

**Framework**: GameKit  
**Kind**: property

The conclusion or results of a participant in a match.

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
var matchOutcome: GKTurnBasedMatch.Outcome { get set }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Initially, GameKit sets this property to [`GKTurnBasedMatch.Outcome.none`](gkturnbasedmatch/outcome/none.md). Then before a player forfeits a match or you end a match, set this property to a value that reflects the participant’s outcome. Optionally, set this property to a custom value using an `OR` operation that fits in the range specified by the [`GKTurnBasedMatch.Outcome.customRange`](gkturnbasedmatch/outcome/customrange.md) enumeration case.

## See Also

- [GKTurnBasedMatch.Outcome](gkturnbasedmatch/outcome.md)
  The state of a participant when they forfeit a match or when a match ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/matchoutcome)*