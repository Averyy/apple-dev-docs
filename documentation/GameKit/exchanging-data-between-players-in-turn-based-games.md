# Exchanging data between players in turn-based games

**Framework**: GameKit

Add the ability for players to exchange game data and send messages while waiting for their turns.

#### Overview

You can increase engagement in turn-based games by letting participants communicate and exchange data while they wait for the current participant to take their turn.

To implement this feature, provide an interface in your game where participants can communicate — for example, exchange items in the game. Then initiate an exchange request from the user of your game instance, called the , to one or more recipients. GameKit handles the requests between participants and the status of the exchange object as participants reply. You implement protocol methods to accept exchanges, display results, and save completed exchanges. When you save completed exchanges, GameKit notifies all other participants.

To receive the protocol messages, register as a listener of the local player, and conform to the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol. For more information, see [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

```swift
GKLocalPlayer.local.register(self)
```

> ❗ **Important**:  The code examples in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details about asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

 The code examples in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details about asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

##### Send Exchange Requests

Any participant, including the current participant who is taking their turn, can send an exchange request to one or more other participants. When sending an exchange request, you pass the recipients, the game-specific exchange data, and a localized message to the `GKTurnBasedMatch` [`sendExchange(to:data:localizableMessageKey:arguments:timeout:completionHandler:)`](gkturnbasedmatch/sendexchange(to:data:localizablemessagekey:arguments:timeout:completionhandler:).md) method.

```swift
try await match.sendExchange(to: participants, data: data!, localizableMessageKey: 
   "This is my exchange request.", arguments: [], timeout: GKTurnTimeoutDefault)
```

In the exchange data, provide enough game-specific information for recipients to decide whether to accept or decline the request.

To localize the message, add the key you pass and a placeholder translation to a `.strings` file in your project (for example, the default `Localizable.strings` file). For more information about adapting your game for different languages and regions, see [`Localization`](https://developer.apple.com/documentation/Xcode/localization).

##### Respond to Exchange Requests

When a recipient receives an exchange request, GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) protocol method, passing the exchange object. If your game isn’t running or is in the background, GameKit displays a notification containing the localized message first. When the recipient taps the notification, GameKit launches your game or brings your game back to the foreground, and then invokes the method.

To accept or decline the exchange request on behalf of the participant, implement the [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) method using the following steps:

1. Unarchive the exchange data in the [`GKTurnBasedExchange`](gkturnbasedexchange.md) object that GameKit passes to this method.
2. If the status property is [`GKTurnBasedExchangeStatus.active`](gkturnbasedexchangestatus/active.md), present an interface containing the exchange data that lets the recipient accept or decline the request.
3. To display more details to the recipient, use the other `GKTurnBasedExchange` properties, such as the [`sender`](gkturnbasedexchange/sender.md) and [`message`](gkturnbasedexchange/message.md) properties.
4. If the recipient accepts the exchange request, invoke the [`reply(withLocalizableMessageKey:arguments:data:completionHandler:)`](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md) method. Optionally, pass additional exchange information back to the sender using the `data` parameter.

##### Save Completed Exchanges

When all recipients reply to an exchange request or requests time out, GameKit invokes the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) method in the current participant’s game instance and the original sender’s game instance.

GameKit passes the exchange object with the status property of [`GKTurnBasedExchangeStatus.complete`](gkturnbasedexchangestatus/complete.md) and the recipient details ([`GKTurnBasedExchangeReply`](gkturnbasedexchangereply.md) objects) in the `replies` parameter. Optionally, present the replies along with their messages and exchange data to the original sender.

If the local player is the current participant, implement the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) method to resolve and save the exchange data. Also, save completed exchanges before the current participant ends their turn, forfeits the match, or ends the match.

1. Add your game-specific exchange data to the match data that you save in Game Center and send to participants. For example, add code that transfers items between participants or saves their conversations.
2. Invoke the [`saveMergedMatch(_:withResolvedExchanges:completionHandler:)`](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md) method, passing the current match data, including any exchange data, and the completed exchange objects. This method removes the exchanges from the match’s [`completedExchanges`](gkturnbasedmatch/completedexchanges.md) and [`exchanges`](gkturnbasedmatch/exchanges.md) properties.

Only the current participant can invoke the [`saveMergedMatch(_:withResolvedExchanges:completionHandler:)`](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md) method, even if the current participant isn’t involved in the exchanges.

##### Display Exchange Results

When the current participant saves completed exchanges with match data, GameKit invokes the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method in each participant game instance. Implement this method to present the new match data, including the exchange data. For example, show the items that transfer between participants and recipient reply messages.

##### Cancel Exchange Requests

You can cancel an exchange request anytime before the current participant saves it and the status property becomes [`GKTurnBasedExchangeStatus.resolved`](gkturnbasedexchangestatus/resolved.md). To cancel an exchange request, use the `GKTurnBasedExchange` [`cancel(withLocalizableMessageKey:arguments:completionHandler:)`](gkturnbasedexchange/cancel(withlocalizablemessagekey:arguments:completionhandler:).md) method. Pass a localizable message that GameKit displays in a notification if the recipient isn’t running your game or it’s in the background.

```swift
try await exchange.cancel(withLocalizableMessageKey: "I'm canceling the exchange request.", arguments: [])
```

To update the gameplay interface and display the message when a participant cancels an exchange request, implement the [`player(_:receivedExchangeCancellation:for:)`](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md) protocol method.

## See Also

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
  Let Game Center store and forward match data between players in a turn-based game.
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)
  Notify players of match events by sending messages and game data.
- [class GKTurnBasedMatchmakerViewController](gkturnbasedmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a turn-based match and automatch to fill any empty slots.
- [class GKTurnBasedMatch](gkturnbasedmatch.md)
  An object that encapsulates the match data for games where players take turns.
- [class GKTurnBasedParticipant](gkturnbasedparticipant.md)
  A participant in a turn-based match.
- [protocol GKTurnBasedEventListener](gkturnbasedeventlistener.md)
  The protocol that handles turn-based and data-exchange events between participants in a match.
- [class GKTurnBasedExchange](gkturnbasedexchange.md)
  Exchange request information that participants send in a turn-based match.
- [class GKTurnBasedExchangeReply](gkturnbasedexchangereply.md)
  Details about a recipient’s response to an exchange request.
- [GKGameCenterBadgingDisabled](../BundleResources/Information-Property-List/GKGameCenterBadgingDisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/exchanging-data-between-players-in-turn-based-games)*