# Sending messages to players in turn-based games

**Framework**: GameKit

Notify players of match events by sending messages and game data.

#### Overview

GameKit provides several APIs for you to communicate events and send messages in your turn-based games. You can include a message and custom game data in the [`GKTurnBasedMatch`](gkturnbasedmatch.md) object passed between active participants. You can also send a notification to other participants when they’re not running your game.

To send other types of data between players when they’re not taking their turn, see the [`GKTurnBasedExchange`](gkturnbasedexchange.md) class.

> ❗ **Important**:  The code listings in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details on asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

 The code listings in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details on asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

##### Pass Messages From the Current Participant

You can send localized or non-localized messages from the current participant to others in a turn-based match using the [`GKTurnBasedMatch`](gkturnbasedmatch.md) object. If the game isn’t running or is in the background, the message you provide appears immediately at the top of the screen as a notification. If the game is in the foreground, get the message from the match object GameKit passes to participants and display it in your own interface.

Before you perform an action such as ending a turn, set the [`message`](gkturnbasedmatch/message.md) property of the match object. Alternatively, set a message that GameKit localizes using the receiving participant’s language and region settings using the [`setLocalizableMessageWithKey(_:arguments:)`](gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:).md) method.

```swift
match.message = "We're all counting on you!"
try await match.endTurn(withNextParticipants: nextParticipants, turnTimeout: GKTurnTimeoutDefault, match: gameData)
```

If a participant taps the notification when it appears, GameKit launches the game or brings it to the foreground. GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) protocol method passing [`true`](https://developer.apple.com/documentation/swift/true) as the active parameter. Implement this method to join the match. For more information on handling turn-based events, see [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

If the game is in the foreground, GameKit invokes this method but passes [`false`](https://developer.apple.com/documentation/swift/false) as the active parameter. You can then present the message in your own interface by getting the message from the match object using the [`message`](gkturnbasedmatch/message.md) property.

To localize a message, add the key you pass to the [`setLocalizableMessageWithKey(_:arguments:)`](gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:).md) method and a placeholder translation to a `.strings` file in your project (for example, the default `Localizable.strings` file). For more information on adapting your game for different languages and regions, see [`Localization`](https://developer.apple.com/documentation/Xcode/localization).

##### Send Messages From Any Participant

Send a localized message from any participant to others using a Game Center notification. For example, send a reminder to the current participant from another participant who is waiting for them to take their turn. GameKit sends the reminder to the participants as a push notification that doesn’t interrupt their gameplay. The notification only appears when the game isn’t running — it doesn’t appear if the participant runs the game in either the foreground or background.

![A screenshot of the Game Center notification reminder at the top of a phone screen. The notification shows the game name at the top and the message “It’s your turn to play.” at the bottom.](https://docs-assets.developer.apple.com/published/b24487f35ecf2f8cf71f5423f8a14224/media-3894240%402x.png)

To display the GameKit notification:

1. Invoke the `GKTurnBasedMatch` [`sendReminder(to:localizableMessageKey:arguments:completionHandler:)`](gkturnbasedmatch/sendreminder(to:localizablemessagekey:arguments:completionhandler:).md) method passing the participants and a localized message key:

```swift
// Create an array that contains the current participant.
let participants = match.participants.filter {
    $0 == match.currentParticipant
}

// Send a reminder to the current participant.
try await match.sendReminder(to: participants, localizableMessageKey: "It's your turn to play.", arguments: [])
```

1. Add the localized message key and placeholder translation to a  `.strings` file in your project. If necessary, add a `.strings` file (for example, the default `Localizable.strings` file) to your project and make it localizable. For the Xcode steps, see [`Adding resources to localizations`](https://developer.apple.com/documentation/Xcode/adding-resources-to-localizations) and `Editing XLIFF and strings files`.

```swift
"It's your turn to play." = "It's your turn to play.";
```

When the player taps the notification, GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) protocol method passing [`true`](https://developer.apple.com/documentation/swift/true) as the active parameter. Implement this method to join the existing match. For more information on handling turn-based events, see [`Starting turn-based matches and passing turns between players`](starting-turn-based-matches-and-passing-turns-between-players.md).

> **Note**:  If you exceed the system’s 10-minute limit for the frequency of sending reminders, a `GKServerTurnBasedMaxSessionOtherError` error occurs.

 If you exceed the system’s 10-minute limit for the frequency of sending reminders, a `GKServerTurnBasedMaxSessionOtherError` error occurs.

## See Also

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
  Let Game Center store and forward match data between players in a turn-based game.
- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)
  Add the ability for players to exchange game data and send messages while waiting for their turns.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/sending-messages-to-players-in-turn-based-games)*