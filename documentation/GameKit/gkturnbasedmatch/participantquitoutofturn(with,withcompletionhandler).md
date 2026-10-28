# participantQuitOutOfTurn(with:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Forfeits the match on behalf of the local player when it’s not their turn.

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
func participantQuitOutOfTurn(with matchOutcome: GKTurnBasedMatch.Outcome, withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func participantQuitOutOfTurn(with matchOutcome: GKTurnBasedMatch.Outcome) async throws
```

```objc
- (void) participantQuitOutOfTurnWithOutcome:(GKTurnBasedMatchOutcome) matchOutcome withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

Invoke this method to forfeit a match when the local player isn’t the current participant. To receive turn-based events that this method generates, register a listener that conforms to the [`GKTurnBasedEventListener`](../gkturnbasedeventlistener.md) protocol with the local player. See [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md).

## Parameters

- `matchOutcome`: The outcome of the local player who forfeits the match. Don’t pass `nil` as this parameter.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameter:

  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Forfeiting a Match
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](./participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md)
  Forfeits the match on behalf of the local player when it’s their turn.
- [GKTurnBasedMatch.Outcome](./outcome.md)
  The state of a participant when they forfeit a match or when a match ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/participantquitoutofturn(with:withcompletionhandler:))*