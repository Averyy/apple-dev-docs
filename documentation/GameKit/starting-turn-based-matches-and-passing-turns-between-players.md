# Starting turn-based matches and passing turns between players

**Framework**: GameKit

Let Game Center store and forward match data between players in a turn-based game.

#### Overview

In a turn-based game, players take turns to advance gameplay, such as in chess, checkers, and similar board games.

The player who creates a match selects opponents and then takes the first turn. Then you pass the player’s turn, other game data, and the next participant to GameKit. GameKit saves the match data in Game Center, which sends the invitations to the other players. Game Center passes the turn to the next participant who accepts their invitation, until all participants reach an outcome or the match ends.

Players can participate in multiple concurrent matches that continue even after players quit a game. Game Center stores open and completed matches until the player explicitly removes them.

You manage turn-based matches through the GameKit turn-based APIs, specifically by using the [`GKTurnBasedMatch`](gkturnbasedmatch.md) object that Game Center passes between participants. The match object contains the following information:

- Status of the match
- Participants and current participant
- Status and outcomes of individual participants
- A message for participants about the most recent turn
- Your game-specific data

For design guidance, see [`Human Interface Guidelines > Technologies > Game Center > Multiplayer`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-center#Multiplayer).

> ❗ **Important**:  The code examples in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details about asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

 The code examples in this article use GameKit asynchronous methods that you invoke from an `async` method or within a `Task` structure. For details about asynchronous flows, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

##### Create a Match Request

First, create a [`GKMatchRequest`](gkmatchrequest.md) object that contains the parameters of your turn-based game. You can set the number of players, apply groups and attributes to filter the matches, provide an invitation message, and set other criteria.

```swift
let request = GKMatchRequest()
request.minPlayers = 2
request.maxPlayers = 12
```

To get the maximum number of players Game Center supports for turn-based games, pass [`GKMatchType.turnBased`](gkmatchtype/turnbased.md) to the [`maxPlayersAllowedForMatch(of:)`](gkmatchrequest/maxplayersallowedformatch(of:).md) method.

##### Start a Turn Based Match

Let players create a new match and select opponents by using the provided GameKit turn-based interface. Similar to how the process works in the real-time game interface, the player creates a match by tapping the plus button (+) in the upper-right corner. In the next few screens, the player invites players and, optionally, fills empty slots using automatch.

![An iPhone screen showing the turn-based matchmaker view controller interface displaying the participants, and the Invite Friends and the Start Game buttons. ](https://docs-assets.developer.apple.com/published/c6508ddcdd406e0b1fd1c6c87d552e66/media-3894600%402x.png)

In your code, use the following steps to present the turn-based matchmaker interface:

1. Create a [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) object by passing the [`GKMatchRequest`](gkmatchrequest.md) object you configure in the [`Create a match request`](starting-turn-based-matches-and-passing-turns-between-players#Create-a-match-request.md) section above. Set its delegate to your game object that conforms to the [`GKTurnBasedMatchmakerViewControllerDelegate`](gkturnbasedmatchmakerviewcontrollerdelegate.md) protocol.

```swift
let viewController = GKTurnBasedMatchmakerViewController(matchRequest: request)
viewController.turnBasedMatchmakerDelegate = self
```

1. Configure the view controller before presenting it. Optionally, set the view controller’s [`matchmakingMode`](gkturnbasedmatchmakerviewcontroller/matchmakingmode.md) property to limit the use of automatch. You can also set [`showExistingMatches`](gkturnbasedmatchmakerviewcontroller/showexistingmatches.md) to [`false`](https://developer.apple.com/documentation/swift/false) to remove ongoing matches that appear under Your Turn and Their Turn. Otherwise, the player can select an existing match rather than create a new one. For more information about handling existing matches, see the [`Open an existing turn-based match`](starting-turn-based-matches-and-passing-turns-between-players#Open-an-existing-turn-based-match.md) section below.
2. Implement the [`GKTurnBasedMatchmakerViewControllerDelegate`](gkturnbasedmatchmakerviewcontrollerdelegate.md) protocol methods to handle cancellations and errors.
3. Then, present the turn-based matchmaker view controller to the local player.

Alternatively, create your own custom interface, and then programmatically find opponents and accept invitations using the [`find(for:withCompletionHandler:)`](gkturnbasedmatch/find(for:withcompletionhandler:).md), [`acceptInvite(completionHandler:)`](gkturnbasedmatch/acceptinvite(completionhandler:).md), and [`declineInvite(completionHandler:)`](gkturnbasedmatch/declineinvite(completionhandler:).md) methods.

##### Present the Gameplay Interface for the Player to Take Their Turn

Before sending invitations to other players, GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) protocol method for the local player to take the first turn. Later, GameKit invokes this method each time it becomes the player’s turn until the player reaches an outcome or the match ends. Implement this method to present the gameplay interface that lets the player take their turn.

To receive the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) callbacks, conform your game object to the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol and register it with the local player object. Register for callbacks immediately after you authenticate the local player because the system brings your game to the foreground or launches it to deliver important turn-based events. For more information about authentication, see [`Authenticating a player`](authenticating-a-player.md).

```swift
GKLocalPlayer.local.register(self)
```

Then implement the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method to perform the following tasks:

1. Retain the [`GKTurnBasedMatch`](gkturnbasedmatch.md) object that GameKit passes to this method, or retain its [`matchID`](gkturnbasedmatch/matchid.md) property. During gameplay, get the current match object by passing the match ID to the [`loadMatches(completionHandler:)`](gkturnbasedmatch/loadmatches(completionhandler:).md) class method.
2. Update the gameplay interface by obtaining the latest game data from the match object using the [`matchData`](gkturnbasedmatch/matchdata.md) property. If it’s the first turn, the game data is `nil`; otherwise, it’s the game data you set when you pass the turn to the next participant.
3. If the match [`status`](gkturnbasedmatch/status-swift.property.md) property is [`GKTurnBasedMatch.Status.open`](gkturnbasedmatch/status-swift.enum/open.md), configure the gameplay interface according to whose turn it is. Use the [`currentParticipant`](gkturnbasedmatch/currentparticipant.md) property to determine whether it’s the local player’s turn.

```swift
myTurn = GKLocalPlayer.local == match.currentParticipant?.player ? true : false
```

1. Present your gameplay interface to the local player.

##### Pass the Turn to the Next Participant

After the player takes their turn, pass the turn to the next participant based on your game rules and logic. Implement your game to do the following:

1. Create an array of match participants in the order you want Game Center to pass the turn. If communication fails or a participant doesn’t respond, Game Center passes the turn to the next participant in the array. Start with the participants in the [`GKTurnBasedMatch`](gkturnbasedmatch.md) object. For example, exclude the current participant and other participants who, for whatever reason, aren’t active.

```swift
let nextParticipants = match.participants.filter (){
    ($0.status != .done) || ($0 != match.currentParticipant)
}
```

1. Create a `Data` representation of your game data that GameKit saves and forwards to the next participant. Ensure that the size of the match data doesn’t exceed the [`matchDataMaximumSize`](gkturnbasedmatch/matchdatamaximumsize.md) property. For example, use the [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) class to convert your game data to a `Data` object.
2. Call the `GKTurnBasedMatch` [`endTurn(withNextParticipants:turnTimeout:match:completionHandler:)`](gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:).md) method, passing the next participant’s array, current game data, and optional timeout for the participant to take their turn.

```swift
try await match.endTurn(withNextParticipants: nextParticipants, turnTimeout: GKTurnTimeoutDefault, match: gameData)
```

If this is the first turn in the match, Game Center sends the invitations to other participants and then passes the turn to the next participant who accepts their invitation.

Alternatively, use the [`saveCurrentTurn(withMatch:completionHandler:)`](gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:).md) method to save the game data without passing the turn to the next participant. For example, save and forward game data to other participants while the player takes a more complicated, multiple-step turn.

##### Accept Turn Based Match Invitations

After the first turn, Game Center manages the status of participants for you by sending invitations and continuing to fill empty slots if you use automatch.

To join the match, a participant taps the Game Center invitation that appears on their device, and then taps the Accept button. If necessary, the system launches your game or brings it to the foreground. The player can also tap the match under New Invitations in the turn-based matchmaker interface when you present it.

![An iPhone screen showing the Game Center invitation banner that displays the name of the game and an invitation message. Below the banner are the Accept and Decline buttons.](https://docs-assets.developer.apple.com/published/420e6e49674e35e1a288e8aef7eb34d0/media-3894601%402x.png)

When the local player joins a match, GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method. Implement this method to show the gameplay interface with the current game data, and if it’s the local player’s turn, let them take it.

Optionally, implement the [`player(_:didRequestMatchWithOtherPlayers:)`](gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:).md) method to notify the local player when GameKit sends the invitations.

##### Display Participant Details

Enhance your game to show the status, name, and avatar of participants in the match when turn-based events occur. Also, be sure to update your interface when participants decline invitations or forfeit the match.

Implement the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method to perform the following tasks:

1. Get the list of all participants using the `GKTurnBasedMatch` [`participants`](gkturnbasedmatch/participants.md) property and get the participant taking their turn using the [`currentParticipant`](gkturnbasedmatch/currentparticipant.md) property.
2. Show when participants accept their invitations and are actively playing using the `GKTurnBasedParticipant` [`status`](gkturnbasedparticipant/status-swift.property.md) property. During the first turn, the status of other participants is [`GKTurnBasedParticipant.Status.matching`](gkturnbasedparticipant/status-swift.enum/matching.md) because Game Center hasn’t sent the invitations. Later, the status transitions through the [`GKTurnBasedParticipant.Status`](gkturnbasedparticipant/status-swift.enum.md) possible values until the participant exits the match when the status becomes [`GKTurnBasedParticipant.Status.done`](gkturnbasedparticipant/status-swift.enum/done.md).
3. If the [`status`](gkturnbasedparticipant/status-swift.property.md) property is [`GKTurnBasedParticipant.Status.active`](gkturnbasedparticipant/status-swift.enum/active.md), display more details that become available using the [`player`](gkturnbasedparticipant/player.md) property. Display the participant’s name using the `GKPlayer` [`displayName`](gkplayer/displayname.md) property, and their avatar using the [`loadPhoto(for:withCompletionHandler:)`](gkplayer/loadphoto(for:withcompletionhandler:).md) method.

```swift
// Get the opponent's name and avatar.
opponentName = participant.player.displayName
let image = try await participant.player.loadPhoto(for: GKPlayer.PhotoSize.small)
opponentAvatar = Image(uiImage: image)
```

1. If the [`status`](gkturnbasedparticipant/status-swift.property.md) property is [`GKTurnBasedParticipant.Status.done`](gkturnbasedparticipant/status-swift.enum/done.md), show the outcome of the participant using the [`matchOutcome`](gkturnbasedparticipant/matchoutcome.md) property. For example, show whether a participant wins, loses, or forfeits a match.

##### Open an Existing Turn Based Match

A player can continue a match if they don’t forfeit it when they exit or quit your game. In the turn-based matchmaker interface, the player opens an existing match by selecting it under Your Turn or Their Turn.

![An iPhone screen showing the turn-based matchmaker view controller interface displaying the list of existing matches in the Your Turn and Their Turn sections. The Completed Games section displays games that are done. The plus button (+) for creating a new game appears in the upper-right corner.](https://docs-assets.developer.apple.com/published/019eec391c151c4e3e1e06ef0d59b762/media-3901330%402x.png)

When the player selects an open match, GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method. Implement this method to present the match using the current game data in the match object, and if it’s the local player’s turn, let them take it.

GameKit also invokes the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method if the player selects an ended match under Completed and then clicks the View Game button on the next screen.

![An iPhone screen showing the turn-based matchmaker view controller’s completed match detail view. The avatar and name of the player who created the match appear, followed by the View Game button and a list of participants with their avatars, names, and outcomes.](https://docs-assets.developer.apple.com/published/1e6f59285d43d6e39566564df3472d27/media-3894599%402x.png)

If the match [`status`](gkturnbasedmatch/status-swift.property.md) property is [`GKTurnBasedMatch.Status.ended`](gkturnbasedmatch/status-swift.enum/ended.md), show the outcomes of the participants and the final game data from the match object.

If you don’t want existing matches to appear in the interface, set the view controller’s [`showExistingMatches`](gkturnbasedmatchmakerviewcontroller/showexistingmatches.md) to [`false`](https://developer.apple.com/documentation/swift/false) before presenting it.

Alternatively, implement a custom interface that lets players manage existing matches. Use the `GKTurnBasedMatch` [`loadMatches(completionHandler:)`](gkturnbasedmatch/loadmatches(completionhandler:).md) method to load the matches from Game Center.

##### Forfeit a Turn Based Match

A player can forfeit an open match using the turn-based matchmaker interface. The player taps the information button next to a match under Your Turn or Their Turn, and on the next screen, taps the Forfeit button in the upper-right corner. The player can also forfeit a match from the list by sliding the match to the left and tapping the Remove button. Players might also forfeit a match using a control in your gameplay interface.

![An iPhone screen showing the turn-based matchmaker view controller with the open match details. The player’s avatar and name appear at the top with a Play your turn button on the bottom. The Forfeit button appears in the upper-right corner.](https://docs-assets.developer.apple.com/published/cc6831c1e022ab090e7fa7cb9c024f60/media-3894721%402x.png)

GameKit invokes the `GKTurnBasedEventListener` [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method in the game instance of the next participant. If the player removes a match that appears under Completed, GameKit deletes the match from Game Center without notifying your game.

Implement the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) method to update your interface when the status of a participant changes to [`GKTurnBasedParticipant.Status.done`](gkturnbasedparticipant/status-swift.enum/done.md). If the local player can’t continue gameplay because the number of active participants drops below the minimum number of players, end the match, as described in the next section.

To programmatically forfeit a match, call either of the following methods, depending on whether it’s the local player’s turn:

- [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md)
- [`participantQuitOutOfTurn(with:withCompletionHandler:)`](gkturnbasedmatch/participantquitoutofturn(with:withcompletionhandler:).md)

Pass [`GKTurnBasedMatch.Outcome.quit`](gkturnbasedmatch/outcome/quit.md) as the match outcome. If it’s the local player’s turn, pass an array of next participants and the current game data.

```swift
try await match.participantQuitInTurn(with: GKTurnBasedMatch.Outcome.quit, nextParticipants: nextParticipants, turnTimeout: GKTurnTimeoutDefault, match: gameData)
```

When a player forfeits a match, notify participants using the APIs described in [`Sending messages to players in turn-based games`](sending-messages-to-players-in-turn-based-games.md). Optionally, implement the [`player(_:wantsToQuitMatch:)`](gkturnbasedeventlistener/player(_:wantstoquitmatch:).md) protocol method to notify players.

##### End a Turn Based Match

You programmatically end a match depending on your game rules and when participants reach an outcome. You can only end the match when it’s the local player’s turn.

To end a match, set the outcomes of all the participants in the match object using the [`matchOutcome`](gkturnbasedparticipant/matchoutcome.md) property. For example, if the local player wins the match, set the current participant’s outcome to [`GKTurnBasedMatch.Outcome.won`](gkturnbasedmatch/outcome/won.md) and the other participants’ outcomes to [`GKTurnBasedMatch.Outcome.lost`](gkturnbasedmatch/outcome/lost.md).

Then call either of the following methods:

- [`endMatchInTurn(withMatch:completionHandler:)`](gkturnbasedmatch/endmatchinturn(withmatch:completionhandler:).md)
- [`endMatchInTurn(withMatch:leaderboardScores:achievements:completionHandler:)`](gkturnbasedmatch/endmatchinturn(withmatch:leaderboardscores:achievements:completionhandler:).md)

Optionally, pass updated game data, leaderboard scores, and achievements. If the game data doesn’t change, you can pass the existing data.

```swift
try await match.endMatchInTurn(withMatch: match.matchData!)
```

When a match ends, notify the participants using the APIs described in [`Sending messages to players in turn-based games`](sending-messages-to-players-in-turn-based-games.md). Optionally, implement the `GKTurnBasedEventListener` [`player(_:matchEnded:)`](gkturnbasedeventlistener/player(_:matchended:).md) protocol method to notify participants.

## See Also

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)
  Notify players of match events by sending messages and game data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/starting-turn-based-matches-and-passing-turns-between-players)*