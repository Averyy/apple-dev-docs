# Queues

**Framework**: App Store Connect API

Manage the queues that contain matchmaking rule sets and that you submit match requests to.

#### Overview

The `queue` resource represents a queue of match requests that Game Center applies the associated set of matchmaking rules to. For more information, see [`Matchmaking rules`](https://developer.apple.com/documentation/GameKit/matchmaking-rules) in the GameKit framework.

## Topics

### Creating, modifying, and deleting queues
- [Create a queue](post-v1-gamecentermatchmakingqueues.md)
  Create a queue and add it to a rule set.
- [Modify a queue](patch-v1-gamecentermatchmakingqueues-_id_.md)
  Update the properties of a specific queue.
- [Delete a queue](delete-v1-gamecentermatchmakingqueues-_id_.md)
  Delete a specific queue in a rule set.
### Reading queue information
- [List all queues](get-v1-gamecentermatchmakingqueues.md)
  Get information about all queues.
- [Read queue information](get-v1-gamecentermatchmakingqueues-_id_.md)
  Get information about a specific queue and its related objects.
### Objects
- [object GameCenterMatchmakingQueueCreateRequest](gamecentermatchmakingqueuecreaterequest.md)
  The request body you use to create a queue.
- [object GameCenterMatchmakingQueueUpdateRequest](gamecentermatchmakingqueueupdaterequest.md)
  The request body you use to modify a queue.
- [object GameCenterMatchmakingQueueResponse](gamecentermatchmakingqueueresponse.md)
  The response body for endpoints that create, modify, or get a single queue.
- [object GameCenterMatchmakingQueuesResponse](gamecentermatchmakingqueuesresponse.md)
  The response body for endpoints that get multiple queues.
- [object GameCenterMatchmakingQueue](gamecentermatchmakingqueue.md)
  The data structure that represents a queue.

## See Also

- [Rules](rules.md)
  Manage the matchmaking rules that Game Center uses to find players.
- [Expressions](expressions.md)
  Write expressions that query the match requests in a queue to find the best players for a match.
- [Rule sets](rule-sets.md)
  Manage the rule sets that you add matchmaking rules and teams to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Testing](testing.md)
  Test matchmaking rules using sample data.
- [Metrics](metrics.md)
  Analyze data about matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/queues)*