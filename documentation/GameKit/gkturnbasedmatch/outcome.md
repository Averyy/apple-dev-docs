# GKTurnBasedMatch.Outcome

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GKTurnBasedMatchOutcome : NSInteger;
```

## Topics

### Outcomes
- [GKTurnBasedMatch.Outcome.none](./outcome/none.md)
  The participant doesn’t reach an outcome.
- [GKTurnBasedMatch.Outcome.quit](./outcome/quit.md)
  The participant forfeits the match.
- [GKTurnBasedMatch.Outcome.won](./outcome/won.md)
  The participant wins the match.
- [GKTurnBasedMatch.Outcome.lost](./outcome/lost.md)
  The participant loses the match.
- [GKTurnBasedMatch.Outcome.tied](./outcome/tied.md)
  The participant ties the match.
- [GKTurnBasedMatch.Outcome.timeExpired](./outcome/timeexpired.md)
  The match ends because the time limit expires.
- [GKTurnBasedMatch.Outcome.first](./outcome/first.md)
  The participant finishes in first place.
- [GKTurnBasedMatch.Outcome.second](./outcome/second.md)
  The participant finishes in second place.
- [GKTurnBasedMatch.Outcome.third](./outcome/third.md)
  The participant finishes in third place.
- [GKTurnBasedMatch.Outcome.fourth](./outcome/fourth.md)
  The participant finishes in fourth place.
- [GKTurnBasedMatch.Outcome.customRange](./outcome/customrange.md)
  The participant reaches a game-specific outcome.
### Initializers
- [init?(rawValue: Int)](./outcome/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Forfeiting a Match
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md)
  Forfeits the match on behalf of the local player when it’s their turn.
- [func participantQuitOutOfTurn(with: GKTurnBasedMatch.Outcome, withCompletionHandler: (((any Error)?) -> Void)?)](./participantquitoutofturn%28with,withcompletionhandler%29.md)
  Forfeits the match on behalf of the local player when it’s not their turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/outcome)*