# endMatchInTurn(withMatch:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Ends the match.

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
func endMatchInTurn(withMatch matchData: Data) async throws
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Invoke this method only when the local player is the current participant. Also, set the [`matchOutcome`](gkturnbasedparticipant/matchoutcome.md) property for each participant in the match’s [`participants`](gkturnbasedmatch/participants.md) property to a value other than [`GKTurnBasedMatch.Outcome.none`](gkturnbasedmatch/outcome/none.md) before invoking this method.

To receive turn-based events that this method generates, register a listener that conforms to the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol with the local player. See [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

## Parameters

- `matchData`: Your game-specific data representing the match state. For example, include information needed for the next participant to take their turn in this object. Don’t pass   as this parameter.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func endMatchInTurn(withMatch: Data, leaderboardScores: [GKLeaderboardScore], achievements: [Any], completionHandler: ((any Error)?) -> Void)](gkturnbasedmatch/endmatchinturn(withmatch:leaderboardscores:achievements:completionhandler:).md)
  Ends the match while submitting scores and achievements for all of the participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endmatchinturn(withmatch:completionhandler:))*