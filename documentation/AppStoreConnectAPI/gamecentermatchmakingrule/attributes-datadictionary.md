# GameCenterMatchmakingRule.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes of a matchmaking rule.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRule.Attributes
```

## Properties

- `description` (string): A human-readable description of the rule.
- `expression` (string): Code that returns a Boolean or numeric value that the matchmaking rules algorithm executes to compare or filter match requests.
- `referenceName` (string): A name for the rule that’s unique within the scope of its rule set.
- `type` (string): The type or category of the rule that determines the return value and properties available in the expression.
- `weight` (number): A numeric value for the rule when `type` is either `DISTANCE` or `MATCH`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrule/attributes-data.dictionary)*