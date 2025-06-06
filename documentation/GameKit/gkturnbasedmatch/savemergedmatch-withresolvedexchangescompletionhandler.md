# saveMergedMatch(_:withResolvedExchanges:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Saves match data for completed exchanges without ending the turn.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func saveMergedMatch(_ matchData: Data, withResolvedExchanges exchanges: [GKTurnBasedExchange]) async throws
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

Use this method to save the exchange data in the match’s [`completedExchanges`](gkturnbasedmatch/completedexchanges.md) property before the current participant ends their turn, forfeits a match, or ends a match. Alternatively, invoke this method from the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) protocol method as recipients reply to individual exchange requests.

This method removes the exchanges from the current participant’s `completedExchanges` property and all participant’s [`exchanges`](gkturnbasedmatch/exchanges.md) property. So retain your game-specific exchange data and merge it into the match data, before you invoke this method.

## Parameters

- `matchData`: Your game-specific data representing the match state including the resolved exchange data.
- `exchanges`: The completed exchanges that you resolve or merge into the match data.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func sendExchange(to: [GKTurnBasedParticipant], data: Data, localizableMessageKey: String, arguments: [String], timeout: TimeInterval, completionHandler: ((GKTurnBasedExchange?, (any Error)?) -> Void)?)](gkturnbasedmatch/sendexchange(to:data:localizablemessagekey:arguments:timeout:completionhandler:).md)
  Sends an exchange request that contains your game data to one or more participants.
- [Exchange Timeouts](exchange-timeouts.md)
  The amount of time that passes before an exchange times out.
- [var exchangeDataMaximumSize: Int](gkturnbasedmatch/exchangedatamaximumsize.md)
  The maximum size of the exchange data.
- [var exchangeMaxInitiatedExchangesPerPlayer: Int](gkturnbasedmatch/exchangemaxinitiatedexchangesperplayer.md)
  The maximum number of exchanges the local player can initiate.
- [var activeExchanges: [GKTurnBasedExchange]?](gkturnbasedmatch/activeexchanges.md)
  The exchanges that the local player needs to accept or reject.
- [var completedExchanges: [GKTurnBasedExchange]?](gkturnbasedmatch/completedexchanges.md)
  The exchange requests that all recipients replied to and the current participant needs to save.
- [var exchanges: [GKTurnBasedExchange]?](gkturnbasedmatch/exchanges.md)
  The exchange requests that are active or complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:))*