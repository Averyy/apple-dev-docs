# GameCenterMatchmakingRuleSet

**Framework**: App Store Connect API  
**Kind**: dictionary

A named collection of matchmaking rules and queues that defines the logic for matching players in a Game Center game.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleSet
```

## Topics

### Objects
- [object GameCenterMatchmakingRuleSet.Attributes](gamecentermatchmakingruleset/attributes-data.dictionary.md)
  The attributes of the rule set.
- [object GameCenterMatchmakingRuleSet.Relationships](gamecentermatchmakingruleset/relationships-data.dictionary.md)
  The relationships to other objects belonging to the rule set.

## Properties

- `attributes` (GameCenterMatchmakingRuleSet.Attributes): The attributes of the rule set.
- `id` (string) *(required)*: The unique identifier for the rule set.
- `links` (ResourceLinks)
- `relationships` (GameCenterMatchmakingRuleSet.Relationships): The relationships to other objects belonging to the rule set.
- `type` (string) *(required)*: The type of resource.

## See Also

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
- [object GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse](gamecentermatchmakingrulesetmatchmakingqueueslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetRulesLinkagesResponse](gamecentermatchmakingrulesetruleslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetTeamsLinkagesResponse](gamecentermatchmakingrulesetteamslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingruleset)*