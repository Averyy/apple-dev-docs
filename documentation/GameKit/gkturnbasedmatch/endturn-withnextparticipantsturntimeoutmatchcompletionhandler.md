# endTurn(withNextParticipants:turnTimeout:match:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Passes the turn from the current participant to the next participant.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func endTurn(withNextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: TimeInterval, match matchData: Data) async throws
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Invoke this method only when the local player is the current participant. To receive turn-based events that this method generates, register a listener that conforms to the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol with the local player. See [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

## Parameters

- `nextParticipants`: Match participants in the order you want Game Center to pass the turn. Game Center passes the turn to the next participant in the array when communication fails or a participant doesn’t finish their turn within the time limit. Elements in this array must be in the   property.
- `timeout`: The length of time a participant has to complete their turn before Game Center passes the turn to the next participant. The maximum value is 90 days.
- `matchData`: Your game-specific data representing the match state. For example, include information needed for the next participant to take their turn in this object. Don’t pass   as this parameter.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func saveCurrentTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:).md)
  Saves your match data in Game Center without ending the turn.
- [Turn Timeouts](turn-timeouts.md)
  A timeout for a player to take their turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:))*