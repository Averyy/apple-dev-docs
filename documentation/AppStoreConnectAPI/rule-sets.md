# Rule sets

**Framework**: App Store Connect API

Manage the rule sets that you add matchmaking rules and teams to.

#### Overview

The `rule set` resource represents a set of rules associated with a queue that Game Center applies to match requests in the queue. For more information, see [`Matchmaking rules`](https://developer.apple.com/documentation/GameKit/matchmaking-rules) in the GameKit framework.

## Topics

### Creating, modifying, and deleting rule sets
- [Create a rule set](post-v1-gamecentermatchmakingrulesets.md)
  Create a rule set to contain matchmaking rules and teams.
- [Modify a rule set](patch-v1-gamecentermatchmakingrulesets-_id_.md)
  Update the attributes of a rule set.
- [Delete a rule set](delete-v1-gamecentermatchmakingrulesets-_id_.md)
  Delete a rule set along with its matchmaking rules and teams.
### Reading rule set information
- [List all rule sets](get-v1-gamecentermatchmakingrulesets.md)
  Get information about all rule sets and their associated objects.
- [Read rule set information](get-v1-gamecentermatchmakingrulesets-_id_.md)
  Get information about a specific rule set and its related objects.
- [List queues in a rule set](get-v1-gamecentermatchmakingrulesets-_id_-matchmakingqueues.md)
  Get information about queues that belong to a rule set.
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/matchmakingQueues](get-v1-gamecentermatchmakingrulesets-_id_-relationships-matchmakingqueues.md)
- [List rules in a rule set](get-v1-gamecentermatchmakingrulesets-_id_-rules.md)
  Get information about the rules in a rule set.
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/rules](get-v1-gamecentermatchmakingrulesets-_id_-relationships-rules.md)
- [List teams in a rule set](get-v1-gamecentermatchmakingrulesets-_id_-teams.md)
  Get information about the teams in a rule set.
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/teams](get-v1-gamecentermatchmakingrulesets-_id_-relationships-teams.md)
### Objects
- [object GameCenterMatchmakingRuleSetCreateRequest](gamecentermatchmakingrulesetcreaterequest.md)
  The request body you use to create a rule set.
- [object GameCenterMatchmakingRuleSetUpdateRequest](gamecentermatchmakingrulesetupdaterequest.md)
  The request body you use to modify a rule set.
- [object GameCenterMatchmakingRuleSetResponse](gamecentermatchmakingrulesetresponse.md)
  The response body for endpoints that create, modify, or get a single rule.
- [object GameCenterMatchmakingRuleSetsResponse](gamecentermatchmakingrulesetsresponse.md)
  The response body for endpoints that get multiple rule sets.
- [object GameCenterMatchmakingRulesResponse](gamecentermatchmakingrulesresponse.md)
  The response body for endpoints that get multiple rules.
- [object GameCenterMatchmakingRuleSet](gamecentermatchmakingruleset.md)
  The data structure that represents a rule set.
- [object GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse](gamecentermatchmakingrulesetmatchmakingqueueslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetRulesLinkagesResponse](gamecentermatchmakingrulesetruleslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetTeamsLinkagesResponse](gamecentermatchmakingrulesetteamslinkagesresponse.md)

## See Also

- [Rules](rules.md)
  Manage the matchmaking rules that Game Center uses to find players.
- [Expressions](expressions.md)
  Write expressions that query the match requests in a queue to find the best players for a match.
- [Queues](queues.md)
  Manage the queues that contain matchmaking rule sets and that you submit match requests to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Testing](testing.md)
  Test matchmaking rules using sample data.
- [Metrics](metrics.md)
  Analyze data about matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/rule-sets)*