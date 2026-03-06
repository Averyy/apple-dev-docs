# GameCenterMatchmakingRuleSet.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes of the rule set.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleSet.Attributes
```

## Properties

- `maxPlayers` (integer): The maximum number of players who can join the matches that Game Center finds using these rules.
- `minPlayers` (integer): The minimum number of players who can join the matches that Game Center finds using these rules.
- `referenceName` (string): A name for the rule set that’s unique within the scope of your development team.
- `ruleLanguageVersion` (integer): The version of the expression language that all the rules in this rule set use. The only possible value is `1`.

## See Also

- [object GameCenterMatchmakingRuleSet.Relationships](gamecentermatchmakingruleset/relationships-data.dictionary.md)
  The relationships to other objects belonging to the rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingruleset/attributes-data.dictionary)*