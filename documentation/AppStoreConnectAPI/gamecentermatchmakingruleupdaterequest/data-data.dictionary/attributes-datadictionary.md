# GameCenterMatchmakingRuleUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes of a rule that you modify.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingRuleUpdateRequest.Data.Attributes
```

## Properties

- `description` (string): A human-readable description of the rule.
- `expression` (string): Code that returns a Boolean or numeric value that the matchmaking rules algorithm executes to compare or filter match requests.
- `weight` (number): A numeric value for the rule when `type` is either `DISTANCE` or `MATCH`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingruleupdaterequest/data-data.dictionary/attributes-data.dictionary)*