# GKTurnBasedMatch.Outcome

**Framework**: GameKit  
**Kind**: enum

The state of a participant when they forfeit a match or when a match ends.

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
enum Outcome
```

## Topics

### Outcomes
- [GKTurnBasedMatch.Outcome.none](gkturnbasedmatch/outcome/none.md)
  The participant doesn’t reach an outcome.
- [GKTurnBasedMatch.Outcome.quit](gkturnbasedmatch/outcome/quit.md)
  The participant forfeits the match.
- [GKTurnBasedMatch.Outcome.won](gkturnbasedmatch/outcome/won.md)
  The participant wins the match.
- [GKTurnBasedMatch.Outcome.lost](gkturnbasedmatch/outcome/lost.md)
  The participant loses the match.
- [GKTurnBasedMatch.Outcome.tied](gkturnbasedmatch/outcome/tied.md)
  The participant ties the match.
- [GKTurnBasedMatch.Outcome.timeExpired](gkturnbasedmatch/outcome/timeexpired.md)
  The match ends because the time limit expires.
- [GKTurnBasedMatch.Outcome.first](gkturnbasedmatch/outcome/first.md)
  The participant finishes in first place.
- [GKTurnBasedMatch.Outcome.second](gkturnbasedmatch/outcome/second.md)
  The participant finishes in second place.
- [GKTurnBasedMatch.Outcome.third](gkturnbasedmatch/outcome/third.md)
  The participant finishes in third place.
- [GKTurnBasedMatch.Outcome.fourth](gkturnbasedmatch/outcome/fourth.md)
  The participant finishes in fourth place.
- [GKTurnBasedMatch.Outcome.customRange](gkturnbasedmatch/outcome/customrange.md)
  The participant reaches a game-specific outcome.
### Initializers
- [init?(rawValue: Int)](gkturnbasedmatch/outcome/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md)
  Forfeits the match on behalf of the local player when it’s their turn.
- [func participantQuitOutOfTurn(with: GKTurnBasedMatch.Outcome, withCompletionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitoutofturn(with:withcompletionhandler:).md)
  Forfeits the match on behalf of the local player when it’s not their turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/outcome)*