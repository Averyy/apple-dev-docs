# sendExchange(to:data:localizableMessageKey:arguments:timeout:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sends an exchange request that contains your game data to one or more participants.

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
func sendExchange(to participants: [GKTurnBasedParticipant], data: Data, localizableMessageKey key: String, arguments: [String], timeout: TimeInterval) async throws -> GKTurnBasedExchange
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

If your game isn’t running or is in the background on recipient devices, a notification containing the localized message you pass to this method appears. When the participant taps or clicks the notification, GameKit launches or brings the game to the foreground and then invokes the [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) method.

Implement the [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) protocol method to handle the exchange request — for example, show an interface on the receiver’s device to accept or reject the exchange.

## Parameters

- `participants`: The other participants, excluding the local player and inactive participants, that GameKit sends the exchange request to.
- `data`: The data that GameKit sends to the other participants.
- `key`: The identifier for looking up the translated message in the default   file. If you use a formatted string with specifiers, provide the arguments.
- `arguments`: A list of arguments to substitute into the localized string if it’s formatted and contains specifiers.
- `timeout`: The length of time a participant has to respond to the exchange request. The maximum value is 90 days.
- `completionHandler`: The block receives the following parameters:

## See Also

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
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md)
  Saves match data for completed exchanges without ending the turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/sendexchange(to:data:localizablemessagekey:arguments:timeout:completionhandler:))*