# Matchmaking rules

**Framework**: GameKit

Game Center applies different type of rules you create in a particular order to find the best matches.

#### Overview

With matchmaking rules, you have finer control over automatch of players to fill empty slots in peer-to-peer and hosted match requests. During development, you use the matchmaking rules APIs to upload your rules to the Game Center server. You group rules into rule sets and assign the rule sets to queues. In your game code, you configure match requests to use your set of matchmaking rules by specifying a queue. Game Center applies your rules to all the match requests in the queue to fill the empty slots.

![A flow chart of the matchmaking rules architecture showing you uploading your matchmaking rules, players sending match requests to  Game Center, and Game Center adding them to the queue and applying your rules.](https://docs-assets.developer.apple.com/published/bf2ecf9990b6345a5a64eebbe8e7a40e/media-4306607%402x.png)

You group rules into sets for each configuration, feature, or purpose in your game and associate the rule sets with a queue. Game instances submit match requests to specific queues, and Game Center applies the corresponding rules to the match requests in that queue. The rules contain an expression that behaves like a query to filter and prioritize the requests. Game Center finds the most compatible players that meet your criteria, in a reasonable amount of time.

For more information on this feature, see [`Meet rule-based matchmaking in Game Center`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111376/).

##### The Matchmaking Rules Algorithm

When finding players using matchmaking rules, Game Center applies four different types of rules to match requests in the queue, along with performing other steps in the algorithm. Game Center applies the expression of the rule, which is a [`JMESPath`](https://developer.apple.comhttps://jmespath.org) formatted string with some Game Center matchmaking function additions. Depending on the type of rule, Game Center evaluates the expression on two or more match requests in the queue.

![A flow chart of the matchmaking algorithm that shows Game Center applying compatible, distance, match, and team rules in sequence. After applying each type of rule, Game Center filters the match request, except for distance rules that sort match requests, until it has match candidates. If team rules exist, Game Center separates the match requests into teams.](https://docs-assets.developer.apple.com/published/55f79f7a2df92dc4d332d2aa0f9ea559/media-4306609%402x.png)

Game Center performs the following steps in sequence:

- Sorts the match requests in a queue by age of the request to minimize player wait time and then applies compatible rules to pairs of requests.  compare two requests and return a Boolean value that indicates whether the requests are compatible. If all the compatible rules return [`true`](https://developer.apple.com/documentation/swift/true), Game Center continues processing the pair. For example, requiring the app version to be 2.0 and above is a compatible rule.
- Applies the distance rules to pairs of compatible requests.  compare two requests and return a numeric value between `0.0` and `1.0`. Game Center uses the value to prioritize similar requests, where `0.0` is the most similar and `1.0` is the least similar. For example, requiring the geo latency between players to be low is a distance rule.
- Prioritizes compatible matches by age and distance, and generates candidate matches that have the most number of players within the range that you specify in the rule set. Sorts candidate matches by age and applies the match rules.  apply to a set of matches and return a Boolean value that indicates whether the requests are valid matches. For example, requiring a range in skill level between `0` and `5` is a match rule.
- Generates candidate teams from combinations of candidate matches and applies the team rules, If you add rules to assign players to teams.  apply to a set of teams containing players and return a Boolean value that indicates whether the teams satisfy a constraint. For example, ensuring that the total skill difference between teams is less than `1` is a team rule.

For more information on matchmaking rules with examples, see [`Finding players using matchmaking rules`](finding-players-using-matchmaking-rules.md). For details on the matchmaking REST APIs, see Matchmaking rules in App Store Connect API.

## Topics

### Essentials
- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
  Create a more customized and optimized gaming experience by using matchmaking rules to find players in a real-time game.
### Rules
- [Letting players join matches using party codes](letting-players-join-matches-using-party-codes.md)
  Add a rule that lets players invite players and join matches using a shared party code.
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)
  Add a rule to find players in a range of skill levels to balance competitive gameplay.
- [Assigning players to teams using rules](assigning-players-to-teams-using-rules.md)
  Set criteria for assigning players to teams in your game using matchmaking rules.
- [Creating matchmaking rules for backward compatibility](creating-matchmaking-rules-for-backward-compatibility.md)
  Add matchmaking rules that support previous classic matchmaking versions of your game.
### Testing
- [Testing matchmaking rules](testing-matchmaking-rules.md)
  Test your matchmaking rules before you use them in your game.
- [Troubleshooting matchmaking rules using metrics](troubleshooting-matchmaking-rules-using-metrics.md)
  Investigate issues with Game Center by evaluating your matchmaking rules using metrics endpoints.
- [Testing rule sets with player traffic using metrics](testing-rule-sets-with-player-traffic-using-metrics.md)
  Get metrics on a new rule set with real match requests before releasing it.

## See Also

- [Game Center](../AppStoreConnectAPI/game-center.md)
  Manage Game Center data and configurations for your apps.
- [Creating real-time games](creating-real-time-games.md)
  Develop games where multiple players interact in real time.
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
  Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)
  Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [class GKMatchRequest](gkmatchrequest.md)
  An object that encapsulates the parameters to create a real-time or turn-based match.
- [class GKMatchmaker](gkmatchmaker.md)
  An object that creates matches with other players without presenting an interface to the players.
- [class GKMatchmakerViewController](gkmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.
- [protocol GKInviteEventListener](gkinviteeventlistener.md)
  A protocol that handles invite events from Game Center.
- [class GKInvite](gkinvite.md)
  An invitation to join a match sent to the local player from another player.
- [class GKMatch](gkmatch.md)
  A peer-to-peer network between a group of players that sign into Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/matchmaking-rules)*