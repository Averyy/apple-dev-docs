# exchanges

**Framework**: GameKit  
**Kind**: property

The exchange requests that are active or complete.

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
var exchanges: [GKTurnBasedExchange]? { get }
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

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
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md)
  Saves match data for completed exchanges without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/exchanges)*