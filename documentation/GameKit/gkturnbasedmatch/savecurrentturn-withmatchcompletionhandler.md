# saveCurrentTurn(withMatch:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Saves your match data in Game Center without ending the turn.

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
func saveCurrentTurn(withMatch matchData: Data) async throws
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Invoke this method only when the local player is the current participant. To receive turn-based events that this method generates, register a listener that conforms to the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol with the local player. See [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

## Parameters

- `matchData`: Your game-specific data representing the match state. For example, include the current participant’s activity while taking their turn in this object. Don’t pass   as this parameter.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:).md)
  Passes the turn from the current participant to the next participant.
- [Turn Timeouts](turn-timeouts.md)
  A timeout for a player to take their turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:))*