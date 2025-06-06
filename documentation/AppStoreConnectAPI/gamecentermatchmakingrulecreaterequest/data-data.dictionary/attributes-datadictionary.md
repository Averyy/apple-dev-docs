# GameCenterMatchmakingRuleCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes for a rule that you create.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleCreateRequest.Data.Attributes
```

#### Discussion

The possible values for the `type` field are:

| `COMPATIBLE` | Rules that enforce constraints on two match requests and return a Boolean value.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For example, a rule that requires devices to run the same version of your game, or finds players that share a common language or game settings. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If you set the `type` field to `COMPATIBLE`, compare the two match requests in the `requests` array in your expression, as in:  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `areCompatibleAppVersions(requests[0], requests[1])` |
| --- | --- |
| `DISTANCE` | Rules that evaluate the similarity of two match requests and return a numeric value between `0.0` and `1.0`.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For example, rules that compare the latency or distance between players and find players with the exact same language and region setting. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If you set the `type` field to `DISTANCE`, evaluate the two match requests in the `requests` array in your expression, as in: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `geoLatency(requests[0], requests[1])` |
| `MATCH` | Rules that evaluate properties across all compatible requests.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For example, rules that prefer match candidates with more players but allows less players after a period of time, compare the difference in skill levels of players to a desired skill level that’s a function of time, and find players that have compatible game configurations that loosen over time. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If you set the type field to `MATCH`, use the `requests` array in the expression to get all the compatible matches. |
| `TEAM` | Rules that evaluate the assignment of players to teams and return a Boolean value. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For example, rules that make the number of players on each team the same, balance the skill levels on each team for a fair match, and keep invited friends on the same team. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If you set the `type` field to `TEAM`, use the `teams` array to get all the teams associated with the rule set. |

## See Also

- [object GameCenterMatchmakingRuleCreateRequest.Data.Relationships](gamecentermatchmakingrulecreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other objects that you include when creating a rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulecreaterequest/data-data.dictionary/attributes-data.dictionary)*