# endMatchInTurn(withMatch:leaderboardScores:achievements:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Ends the match while submitting scores and achievements for all of the participants.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func endMatchInTurn(withMatch matchData: Data, leaderboardScores scores: [GKLeaderboardScore], achievements: [Any], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func endMatchInTurn(withMatch matchData: Data, leaderboardScores scores: [GKLeaderboardScore], achievements: [Any]) async throws
```

```objc
- (void) endMatchInTurnWithMatchData:(NSData *) matchData leaderboardScores:(NSArray<GKLeaderboardScore *> *) scores achievements:(NSArray *) achievements completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

## Discussion

Invoke this method only when the local player is the current participant. Also, set the [`matchOutcome`](../gkturnbasedparticipant/matchoutcome.md) property for each participant in the match’s [`participants`](./participants.md) property to a value other than [`GKTurnBasedMatch.Outcome.none`](./outcome/none.md) before invoking this method.

To receive turn-based events that this method generates, register a listener that conforms to the [`GKTurnBasedEventListener`](../gkturnbasedeventlistener.md) protocol with the local player. See [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md).

## Parameters

- `matchData`: Your game-specific data representing the match state. For example, include information needed for the next participant to take their turn in this object. Don’t pass `nil` as this parameter.
- `scores`: The final scores that each participant earns in the match. The scores can be for different leaderboards.
- `achievements`: The achievements that each participant acquires in the match.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameter:

  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Ending a Match
- [func endMatchInTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](./endmatchinturn%28withmatch,completionhandler%29.md)
  Ends the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endmatchinturn(withmatch:leaderboardscores:achievements:completionhandler:))*