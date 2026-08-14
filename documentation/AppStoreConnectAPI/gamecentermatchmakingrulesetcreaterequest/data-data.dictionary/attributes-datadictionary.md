# GameCenterMatchmakingRuleSetCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes for a rule set that you create.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleSetCreateRequest.Data.Attributes
```

#### Discussion

The `minPlayers` and `maxPlayers` attributes constrain the range of players in the match requests. If you don’t set the `GKMatchRequest.`[`minPlayers`](https://developer.apple.com/documentation/gamekit/gkmatchrequest/minplayers) and `GKMatchRequest.`[`maxPlayers`](https://developer.apple.com/documentation/gamekit/gkmatchrequest/maxplayers) properties in your code, the properties default to the rule set `minPlayers` and `maxPlayers` attributes. If you set the [`GKMatchRequest`](https://developer.apple.com/documentation/gamekit/gkmatchrequest) properties, use values that are in the rule set range.

For example, if the match request range is `[2, 4]` and the rule set range is `[2,8]`, Game Center finds players within the `[2, 4]` match request range. However, if the match request range is `[2, 8]` and the rule set range is `[3, 4]`, Game Center ignores the match request properties and finds players within the `[3, 4]` rule set range. If the match request range is `[8, 8]` and the rule set range is `[2, 4]` (outside of the rule set range), Game Center never finds players for that request.

## Properties

- `maxPlayers` (integer) *(required)*: The maximum number of players who can join the matches that Game Center finds using these rules.
- `minPlayers` (integer) *(required)*: The minimum number of players who can join the matches that Game Center finds using these rules.
- `referenceName` (string) *(required)*: A name for the rule set that’s unique within the scope of your development team.
- `ruleLanguageVersion` (integer) *(required)*: The version of the expression language that all the rules in this rule set use. The only possible value is `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulesetcreaterequest/data-data.dictionary/attributes-data.dictionary)*