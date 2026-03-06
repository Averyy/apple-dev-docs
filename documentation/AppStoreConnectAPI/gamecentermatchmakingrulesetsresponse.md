# GameCenterMatchmakingRuleSetsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that get multiple rule sets.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleSetsResponse
```

## Properties

- `data` ([GameCenterMatchmakingRuleSet]) *(required)*: The rule sets that an endpoint gets.
- `included` ([*]): The related objects included in the response.
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterMatchmakingRuleSetCreateRequest](gamecentermatchmakingrulesetcreaterequest.md)
  The request body you use to create a rule set.
- [object GameCenterMatchmakingRuleSetUpdateRequest](gamecentermatchmakingrulesetupdaterequest.md)
  The request body you use to modify a rule set.
- [object GameCenterMatchmakingRuleSetResponse](gamecentermatchmakingrulesetresponse.md)
  The response body for endpoints that create, modify, or get a single rule.
- [object GameCenterMatchmakingRulesResponse](gamecentermatchmakingrulesresponse.md)
  The response body for endpoints that get multiple rules.
- [object GameCenterMatchmakingRuleSet](gamecentermatchmakingruleset.md)
  The data structure that represents a rule set.
- [object GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse](gamecentermatchmakingrulesetmatchmakingqueueslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetRulesLinkagesResponse](gamecentermatchmakingrulesetruleslinkagesresponse.md)
- [object GameCenterMatchmakingRuleSetTeamsLinkagesResponse](gamecentermatchmakingrulesetteamslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulesetsresponse)*