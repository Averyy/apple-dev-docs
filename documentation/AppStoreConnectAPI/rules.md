# Rules

**Framework**: App Store Connect API

Manage the matchmaking rules that Game Center uses to find players.

#### Overview

The `rules` resource represents a matchmaking rule that Game Center applies to match requests in a queue.

With matchmaking rules, you have finer control over automatch of players to fill empty slots in a match request. For example, use matchmaking rules to find compatible players and assign them to teams using game-specific information, such as skill level and other criteria. During development, you use the matchmaking rules APIs to upload your rules to the Game Center server. In your game code, you configure match requests to use your set of matchmaking rules. When you submit the match requests, Game Center applies your rules to the collective match requests from multiple game instances in the queue to fill the empty slots.

For more information, see [`Matchmaking rules`](https://developer.apple.com/documentation/GameKit/matchmaking-rules) in the GameKit framework.

## Topics

### Creating, modifying, and deleting rules
- [Create a rule](post-v1-gamecentermatchmakingrules.md)
  Add a matchmaking rule to a rule set.
- [Modify a rule](patch-v1-gamecentermatchmakingrules-_id_.md)
  Update a specific matchmaking rule in a rule set.
- [Delete a rule](delete-v1-gamecentermatchmakingrules-_id_.md)
  Delete a matchmaking rule in a rule set.
### Objects
- [object GameCenterMatchmakingRuleCreateRequest](gamecentermatchmakingrulecreaterequest.md)
  The request body you use to create a rule.
- [object GameCenterMatchmakingRuleUpdateRequest](gamecentermatchmakingruleupdaterequest.md)
  The request body you use to modify a rule.
- [object GameCenterMatchmakingRuleResponse](gamecentermatchmakingruleresponse.md)
  The response body for endpoints that create or modify a rule.
- [object GameCenterMatchmakingRule](gamecentermatchmakingrule.md)
  The data structure that represents a matchmaking rule.

## See Also

- [Expressions](expressions.md)
  Write expressions that query the match requests in a queue to find the best players for a match.
- [Rule sets](rule-sets.md)
  Manage the rule sets that you add matchmaking rules and teams to.
- [Queues](queues.md)
  Manage the queues that contain matchmaking rule sets and that you submit match requests to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Testing](testing.md)
  Test matchmaking rules using sample data.
- [Metrics](metrics.md)
  Analyze data about matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/rules)*