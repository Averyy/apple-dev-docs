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

The `minPlayers` and `maxPlayers` attributes constrain the range of players in the match requests. If you don’t set the `GKMatchRequest.`[`minPlayers`](https://developer.apple.com/documentation/GameKit/GKMatchRequest/minPlayers) and `GKMatchRequest.`[`maxPlayers`](https://developer.apple.com/documentation/GameKit/GKMatchRequest/maxPlayers) properties in your code, the properties default to the rule set `minPlayers` and `maxPlayers` attributes. If you set the [`GKMatchRequest`](https://developer.apple.com/documentation/GameKit/GKMatchRequest) properties, use values that are in the rule set range.

For example, if the match request range is `[2, 4]` and the rule set range is `[2,8]`, Game Center finds players within the `[2, 4]` match request range. However, if the match request range is `[2, 8]` and the rule set range is `[3, 4]`, Game Center ignores the match request properties and finds players within the `[3, 4]` rule set range. If the match request range is `[8, 8]` and the rule set range is `[2, 4]` (outside of the rule set range), Game Center never finds players for that request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingrulesetcreaterequest/data-data.dictionary/attributes-data.dictionary)*