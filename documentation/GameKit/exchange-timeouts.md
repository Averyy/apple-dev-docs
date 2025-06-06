# Exchange Timeouts

**Framework**: GameKit

The amount of time that passes before an exchange times out.

## Topics

### Timeouts
- [var GKExchangeTimeoutDefault: TimeInterval](gkexchangetimeoutdefault.md)
  A one-day exchange request timeout.
- [var GKExchangeTimeoutNone: TimeInterval](gkexchangetimeoutnone.md)
  An exchange request timeout that doesn’t expire.

## See Also

- [func sendExchange(to: [GKTurnBasedParticipant], data: Data, localizableMessageKey: String, arguments: [String], timeout: TimeInterval, completionHandler: ((GKTurnBasedExchange?, (any Error)?) -> Void)?)](gkturnbasedmatch/sendexchange(to:data:localizablemessagekey:arguments:timeout:completionhandler:).md)
  Sends an exchange request that contains your game data to one or more participants.
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
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md)
  Saves match data for completed exchanges without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/exchange-timeouts)*