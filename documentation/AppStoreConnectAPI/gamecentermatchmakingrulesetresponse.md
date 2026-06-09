# GameCenterMatchmakingRuleSetResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, modify, or get a single rule.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleSetResponse
```

## Properties

- `data` (GameCenterMatchmakingRuleSet) *(required)*: The rule set that you create, modify, or get.
- `included` ([*]): The related objects included in the response.
- `links` (DocumentLinks) *(required)*

## See Also

- [object GameCenterMatchmakingRuleSetCreateRequest](gamecentermatchmakingrulesetcreaterequest.md)
  The request body you use to create a rule set.
- [object GameCenterMatchmakingRuleSetUpdateRequest](gamecentermatchmakingrulesetupdaterequest.md)
  The request body you use to modify a rule set.
- [object GameCenterMatchmakingRuleSetsResponse](gamecentermatchmakingrulesetsresponse.md)
  The response body for endpoints that get multiple rule sets.
- [object GameCenterMatchmakingRulesResponse](gamecentermatchmakingrulesresponse.md)
  The response body for endpoints that get multiple rules.
- [object GameCenterMatchmakingRuleSet](gamecentermatchmakingruleset.md)
  A named collection of matchmaking rules and queues that defines the logic for matching players in a Game Center game.
- [object GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse](gamecentermatchmakingrulesetmatchmakingqueueslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetRulesLinkagesResponse](gamecentermatchmakingrulesetruleslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetTeamsLinkagesResponse](gamecentermatchmakingrulesetteamslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulesetresponse)*