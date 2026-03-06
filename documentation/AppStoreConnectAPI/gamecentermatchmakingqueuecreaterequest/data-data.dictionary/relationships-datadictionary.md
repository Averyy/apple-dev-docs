# GameCenterMatchmakingQueueCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary

The rule sets that you include when creating a queue.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingQueueCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object GameCenterMatchmakingQueueCreateRequest.Data.Relationships.ExperimentRuleSet](gamecentermatchmakingqueuecreaterequest/data-data.dictionary/relationships-data.dictionary/experimentruleset-data.dictionary.md)
  An experimental rule set for testing this queue.
- [object GameCenterMatchmakingQueueCreateRequest.Data.Relationships.ExperimentRuleSet.Data](gamecentermatchmakingqueuecreaterequest/data-data.dictionary/relationships-data.dictionary/experimentruleset-data.dictionary/data-data.dictionary.md)
  The data structure of the request body for an experimental rule set.
- [object GameCenterMatchmakingQueueCreateRequest.Data.Relationships.RuleSet](gamecentermatchmakingqueuecreaterequest/data-data.dictionary/relationships-data.dictionary/ruleset-data.dictionary.md)
  The rule set associated with the queue.

## Properties

- `experimentRuleSet` (GameCenterMatchmakingQueueCreateRequest.Data.Relationships.ExperimentRuleSet): The experimental rule set to test the associated rules with live match requests. If you provide an experimental rule set, Game Center processes the match requests in the queue using both the experimental and the required rule set, except that it doesn’t return the results of the experimental rule set to clients. Then compare the results of the experimental rule set with the production rule set using metrics, such as the [`List all queues`](get-v1-gamecentermatchmakingqueues.md) and [`Read queue information`](get-v1-gamecentermatchmakingqueues-_id_.md) endpoints.
- `ruleSet` (GameCenterMatchmakingQueueCreateRequest.Data.Relationships.RuleSet) *(required)*: The rule set to associate with this queue.

## See Also

- [object GameCenterMatchmakingQueueCreateRequest.Data.Attributes](gamecentermatchmakingqueuecreaterequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes for a queue that you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingqueuecreaterequest/data-data.dictionary/relationships-data.dictionary)*