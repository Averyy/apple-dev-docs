# Request

**Framework**: App Store Connect API

An object that represents a match request in a queue.

#### Overview

Use a `Request` object in the expression of a matchmaking rule to access data in the matchmaking rules. A `Request` object corresponds to a [`GKMatchRequest`](https://developer.apple.com/documentation/gamekit/gkmatchrequest) object that the game creates to submit a match request.

##### Properties

-`appVersion`: The app version of the game that makes the request. -`bundleId`: The bundle ID of the game that makes the request. -`locale`: The language and region that the player who initiates this match request uses. -`maxPlayer`: The maximum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`maxPlayers`](https://developer.apple.com/documentation/gamekit/gkmatchrequest/maxplayers) property that you set when submitting this request. -`minPlayers`: The minimum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`minPlayers`](https://developer.apple.com/documentation/gamekit/gkmatchrequest/minplayers) property that you set when submitting this request. -`platform`: The platform of the game that makes the request. -`playerCount`: The total number of players invited to join the match, including the player who initiates the match request. For example, if the request is for the local player only, the player count is `1`. If the local player invites one friend, the player count is `2`. -`playerId`: A unique identifier for the player who initiates this match request. -`properties`: The properties of the game or player that initiates this match request. -`requestName`: A unique identifier for the request. -`secondsInQueue`: The age of the request in seconds.

## See Also

- [Player](player.md)
  An object that represents a player associated with a match request.
- [Team](team.md)
  A team that you add to a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/request)*