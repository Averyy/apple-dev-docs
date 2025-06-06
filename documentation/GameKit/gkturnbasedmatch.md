# GKTurnBasedMatch

**Framework**: GameKit  
**Kind**: class

An object that encapsulates the match data for games where players take turns.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKTurnBasedMatch
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)

#### Overview

A `GKTurnBasedMatch` object represents a match in a turn-based game that Game Center stores and forwards to participants in the match. In a turn-based game, participants take turns to advance gameplay until they reach an outcome. You end the match when all participants reach an outcome or they can no longer continue.

A turn-based match object contains the status of the match, list of participants, the participant whose turn it is, a message about the last turn, and your game-specific data. You can get more details about the participants through the [`GKTurnBasedParticipant`](gkturnbasedparticipant.md) objects in the [`participants`](gkturnbasedmatch/participants.md) property.

You don’t create turn-based match objects directly. When a match event occurs, GameKit passes the match object to listeners that conform to the [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol. Retain the match object or its match ID in the protocol methods, so you can get the latest match data later during gameplay.

Using the match object passed to `GKTurnBasedEventListener` protocol methods, you can perform these actions on behalf of the local player:

- Save game data
- End a turn
- Forfeit a match
- End a match
- Send a reminder to the participant whose turn it is
- Exchange data between participants
- Remove a completed match from Game Center

When you end a turn, forfeit a match, or end a match, you update the match data and if gameplay can continue, choose the next participant. If you end a match, you set the individual participant outcomes as well.

If you present a [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) object for players to manage their turn-based matches, the player can start a match, accept an invitation, open an existing match, and forfeit a match.

##### Subclassing Notes

Don’t subclass the [`GKTurnBasedMatch`](gkturnbasedmatch.md) class.

## Topics

### Creating a Match
- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](gkturnbasedmatch/find(for:withcompletionhandler:).md)
  Creates a new match or finds an existing match that needs a player.
- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/acceptinvite(completionhandler:).md)
  Accepts an invitation for the local player to join a turn-based match.
- [func declineInvite(completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/declineinvite(completionhandler:).md)
  Declines an invitation for the local player to join a turn-based match.
- [func rematch(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/rematch(completionhandler:).md)
  Creates a new turn-based match with the same participants from an existing match.
### Retrieving Match Details
- [var matchID: String](gkturnbasedmatch/matchid.md)
  A unique identifier for the turn-based match.
- [var creationDate: Date](gkturnbasedmatch/creationdate.md)
  The date that Game Center created the match.
- [var participants: [GKTurnBasedParticipant]](gkturnbasedmatch/participants.md)
  The players that participate in a turn-based match.
- [var currentParticipant: GKTurnBasedParticipant?](gkturnbasedmatch/currentparticipant.md)
  The participant whose turn it is.
- [var status: GKTurnBasedMatch.Status](gkturnbasedmatch/status-swift.property.md)
  The state of the match, such as whether the match is open or has ended.
- [GKTurnBasedMatch.Status](gkturnbasedmatch/status-swift.enum.md)
  The states of a match from when it’s created to when it ends.
- [var matchData: Data?](gkturnbasedmatch/matchdata.md)
  The game-specific data that you store in Game Center and pass between participants through a match object.
- [var matchDataMaximumSize: Int](gkturnbasedmatch/matchdatamaximumsize.md)
  The maximum size of the match data.
- [func loadMatchData(completionHandler: ((Data?, (any Error)?) -> Void)?)](gkturnbasedmatch/loadmatchdata(completionhandler:).md)
  Fetches your game-specific data that you store in Game Center when ending a turn, saving a turn, or leaving a match.
### Ending Turns and Saving Data
- [func endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipants:turntimeout:match:completionhandler:).md)
  Passes the turn from the current participant to the next participant.
- [func saveCurrentTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savecurrentturn(withmatch:completionhandler:).md)
  Saves your match data in Game Center without ending the turn.
- [Turn Timeouts](turn-timeouts.md)
  A timeout for a player to take their turn.
### Forfeiting a Match
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md)
  Forfeits the match on behalf of the local player when it’s their turn.
- [func participantQuitOutOfTurn(with: GKTurnBasedMatch.Outcome, withCompletionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitoutofturn(with:withcompletionhandler:).md)
  Forfeits the match on behalf of the local player when it’s not their turn.
- [GKTurnBasedMatch.Outcome](gkturnbasedmatch/outcome.md)
  The state of a participant when they forfeit a match or when a match ends.
### Ending a Match
- [func endMatchInTurn(withMatch: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endmatchinturn(withmatch:completionhandler:).md)
  Ends the match.
- [func endMatchInTurn(withMatch: Data, leaderboardScores: [GKLeaderboardScore], achievements: [Any], completionHandler: ((any Error)?) -> Void)](gkturnbasedmatch/endmatchinturn(withmatch:leaderboardscores:achievements:completionhandler:).md)
  Ends the match while submitting scores and achievements for all of the participants.
### Sending Messages Between Participants
- [var message: String?](gkturnbasedmatch/message.md)
  A message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.
- [func setLocalizableMessageWithKey(String, arguments: [String]?)](gkturnbasedmatch/setlocalizablemessagewithkey(_:arguments:).md)
  Sends a localized message from the current participant to all other participants when you end a turn, forfeit a match, or end a match.
- [func sendReminder(to: [GKTurnBasedParticipant], localizableMessageKey: String, arguments: [String], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/sendreminder(to:localizablemessagekey:arguments:completionhandler:).md)
  Sends a reminder from one participant to a specific set of other participants.
### Exchanging Data Between Participants
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
- [func saveMergedMatch(Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md)
  Saves match data for completed exchanges without ending the turn.
### Loading Existing Matches
- [class func load(withID: String, withCompletionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/load(withid:withcompletionhandler:).md)
  Loads a specific match with the specified identifier.
- [class func loadMatches(completionHandler: (([GKTurnBasedMatch]?, (any Error)?) -> Void)?)](gkturnbasedmatch/loadmatches(completionhandler:).md)
  Fetches the turn-based matches from Game Center that the local player participates in.
### Deleting a Match from Game Center
- [func remove(completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/remove(completionhandler:).md)
  Removes a match from Game Center that the local player participants in.
### Deprecated Methods
- [func participantQuitInTurn(with: GKTurnBasedMatch.Outcome, nextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/participantquitinturn(with:nextparticipant:match:completionhandler:).md)
  Resigns the current player from the match without ending the match.
- [func endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endmatchinturn(withmatch:scores:achievements:completionhandler:).md)
  Ends the match while submitting all of the scores and achievements.
- [func endTurn(withNextParticipant: GKTurnBasedParticipant, match: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/endturn(withnextparticipant:match:completionhandler:).md)
  Updates the data stored on Game Center for the current match.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
  Let Game Center store and forward match data between players in a turn-based game.
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)
  Notify players of match events by sending messages and game data.
- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)
  Add the ability for players to exchange game data and send messages while waiting for their turns.
- [class GKTurnBasedMatchmakerViewController](gkturnbasedmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a turn-based match and automatch to fill any empty slots.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch)*