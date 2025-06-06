# Testing

**Framework**: App Store Connect API

Test matchmaking rules using sample data.

#### Overview

Use the Testing APIs to apply matchmaking rules to sample match requests and player properties. For more information, see [`Testing matchmaking rules`](https://developer.apple.com/documentation/GameKit/testing-matchmaking-rules).

## Topics

### Applying rule sets to sample requests
- [Test a rule set](post-v1-gamecentermatchmakingrulesettests.md)
  Apply the given rule set to the given sample match requests.
### Objects
- [object GameCenterMatchmakingRuleSetTestCreateRequest](gamecentermatchmakingrulesettestcreaterequest.md)
  The request body for testing the rules in a rule set.
- [object GameCenterMatchmakingRuleSetTestResponse](gamecentermatchmakingrulesettestresponse.md)
  The response body for testing a rule set.
- [object GameCenterMatchmakingRuleSetTest](gamecentermatchmakingrulesettest.md)
  The data structure that represents the results of testing a rule set.
- [object GameCenterMatchmakingTestRequestInlineCreate](gamecentermatchmakingtestrequestinlinecreate.md)
  A data structure that represents a sample match request for testing a rule set.
- [object GameCenterMatchmakingTestPlayerPropertyInlineCreate](gamecentermatchmakingtestplayerpropertyinlinecreate.md)
  A resource object that represents a player’s properties when you create a request.
- [object GameCenterMatchmakingTeamAssignment](gamecentermatchmakingteamassignment.md)
  The data structure that represents the assignment of a player to a team.
- [object Location](location.md)
  A representation of a device location.
- [object Property](property.md)
  A representation of a game-specific property.

## See Also

- [Rules](rules.md)
  Manage the matchmaking rules that Game Center uses to find players.
- [Expressions](expressions.md)
  Write expressions that query the match requests in a queue to find the best players for a match.
- [Rule sets](rule-sets.md)
  Manage the rule sets that you add matchmaking rules and teams to.
- [Queues](queues.md)
  Manage the queues that contain matchmaking rule sets and that you submit match requests to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Metrics](metrics.md)
  Analyze data about matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/testing)*