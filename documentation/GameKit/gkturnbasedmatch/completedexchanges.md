# completedExchanges

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The exchange requests that all recipients replied to and the current participant needs to save.

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
var completedExchanges: [GKTurnBasedExchange]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSArray<GKTurnBasedExchange *> * completedExchanges;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSArray<GKTurnBasedExchange *> * completedExchanges;
```

## Mentions

- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## Discussion

Since only the current participant can save exchanges, this property is `nil` if the local player isn’t the current participant. If the local player is the current player, use the [`saveMergedMatch(_:withResolvedExchanges:completionHandler:)`](./savemergedmatch%28_,withresolvedexchanges,completionhandler%29.md) method to save completed exchanges before ending their turn.

## See Also

### Exchanging Data Between Participants
- [func sendExchange(to: [GKTurnBasedParticipant], data: Data, localizableMessageKey: String, arguments: [String], timeout: TimeInterval, completionHandler: ((GKTurnBasedExchange?, (any Error)?) -> Void)?)](./sendexchange%28to,data,localizablemessagekey,arguments,timeout,completionhandler%29.md)
  Sends an exchange request that contains your game data to one or more participants.
- [Exchange Timeouts](../exchange-timeouts.md)
  The amount of time that passes before an exchange times out.
- [var exchangeDataMaximumSize: Int](./exchangedatamaximumsize.md)
  The maximum size of the exchange data.
- [var exchangeMaxInitiatedExchangesPerPlayer: Int](./exchangemaxinitiatedexchangesperplayer.md)
  The maximum number of exchanges the local player can initiate.
- [var activeExchanges: [GKTurnBasedExchange]?](./activeexchanges.md)
  The exchanges that the local player needs to accept or reject.
- [var exchanges: [GKTurnBasedExchange]?](./exchanges.md)
  The exchange requests that are active or complete.
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](./savemergedmatch%28_,withresolvedexchanges,completionhandler%29.md)
  Saves match data for completed exchanges without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/completedexchanges)*