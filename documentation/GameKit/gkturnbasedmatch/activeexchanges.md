# activeExchanges

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The exchanges that the local player needs to accept or reject.

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
var activeExchanges: [GKTurnBasedExchange]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSArray<GKTurnBasedExchange *> * activeExchanges;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSArray<GKTurnBasedExchange *> * activeExchanges;
```

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
- [var completedExchanges: [GKTurnBasedExchange]?](./completedexchanges.md)
  The exchange requests that all recipients replied to and the current participant needs to save.
- [var exchanges: [GKTurnBasedExchange]?](./exchanges.md)
  The exchange requests that are active or complete.
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](./savemergedmatch%28_,withresolvedexchanges,completionhandler%29.md)
  Saves match data for completed exchanges without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/activeexchanges)*