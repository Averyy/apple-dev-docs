# GameCenterMatchmakingRuleCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes for a rule that you create.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```
object GameCenterMatchmakingRuleCreateRequest.Data.Attributes
```

## Discussion

The possible values for the `type` field are:

| `COMPATIBLE` | Rules that enforce constraints on two match requests and return a Boolean value.  ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) For example, a rule that requires devices to run the same version of your game, or finds players that share a common language or game settings. ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) If you set the `type` field to `COMPATIBLE`, compare the two match requests in the `requests` array in your expression, as in:  ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) `areCompatibleAppVersions(requests[0], requests[1])` |
| --- | --- |
| `DISTANCE` | Rules that evaluate the similarity of two match requests and return a numeric value between `0.0` and `1.0`.  ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) For example, rules that compare the latency or distance between players and find players with the exact same language and region setting. ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) If you set the `type` field to `DISTANCE`, evaluate the two match requests in the `requests` array in your expression, as in: ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) `geoLatency(requests[0], requests[1])` |
| `MATCH` | Rules that evaluate properties across all compatible requests.  ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) For example, rules that prefer match candidates with more players but allows less players after a period of time, compare the difference in skill levels of players to a desired skill level that’s a function of time, and find players that have compatible game configurations that loosen over time. ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) If you set the type field to `MATCH`, use the `requests` array in the expression to get all the compatible matches. |
| `TEAM` | Rules that evaluate the assignment of players to teams and return a Boolean value. ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) For example, rules that make the number of players on each team the same, balance the skill levels on each team for a fair match, and keep invited friends on the same team. ![](https://developer.apple.com/tutorials/images/com.apple.appstoreconnectapi/spacer.png) If you set the `type` field to `TEAM`, use the `teams` array to get all the teams associated with the rule set. |

## Properties

- `description` (string) *(required)*: A human-readable description of the rule.
- `expression` (string) *(required)*: Code that returns a Boolean or numeric value that the matchmaking rules algorithm executes to compare or filter match requests.
- `referenceName` (string) *(required)*: A name for the rule that’s unique within the scope of its rule set.
- `type` (string) *(required)*: The type or category of the rule that determines the return value and properties available in the expression.

  **Allowed Values**: `COMPATIBLE`, `DISTANCE`, `MATCH`, `TEAM`
- `weight` (number): A numeric value for the rule when `type` is either `DISTANCE` or `MATCH`.

## See Also

### Objects
- [object GameCenterMatchmakingRuleCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships to other objects that you include when creating a rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulecreaterequest/data-data.dictionary/attributes-data.dictionary)*