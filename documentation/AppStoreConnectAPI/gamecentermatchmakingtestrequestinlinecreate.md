# GameCenterMatchmakingTestRequestInlineCreate

**Framework**: App Store Connect API  
**Kind**: dictionary

A data structure that represents a sample match request for testing a rule set.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingTestRequestInlineCreate
```

## Topics

### Objects
- [object GameCenterMatchmakingTestRequestInlineCreate.Attributes](gamecentermatchmakingtestrequestinlinecreate/attributes-data.dictionary.md)
  The attributes for a sample match request.
- [object GameCenterMatchmakingTestRequestInlineCreate.Relationships](gamecentermatchmakingtestrequestinlinecreate/relationships-data.dictionary.md)
  The relationships of a match request to other objects.

## Properties

- `attributes` (GameCenterMatchmakingTestRequestInlineCreate.Attributes): The object attributes.
- `id` (string): A unique identifier for the match request.
- `relationships` (GameCenterMatchmakingTestRequestInlineCreate.Relationships): The object relationships.
- `type` (string) *(required)*: The type of resource object.

## See Also

- [object GameCenterMatchmakingRuleSetTestCreateRequest](gamecentermatchmakingrulesettestcreaterequest.md)
  The request body for testing the rules in a rule set.
- [object GameCenterMatchmakingTestRequest](gamecentermatchmakingtestrequest.md)
  The type and ID of test matchmaking request.
- [object GameCenterMatchmakingRuleSetTestResponse](gamecentermatchmakingrulesettestresponse.md)
  The response body for testing a rule set.
- [object GameCenterMatchmakingRuleSetTest](gamecentermatchmakingrulesettest.md)
  A test run of a Game Center matchmaking rule set using simulated player properties to validate the rules.
- [object GameCenterMatchmakingTestPlayerProperty](gamecentermatchmakingtestplayerproperty.md)
  A simulated player attribute used when testing Game Center matchmaking rule sets.
- [object GameCenterMatchmakingTestPlayerPropertyInlineCreate](gamecentermatchmakingtestplayerpropertyinlinecreate.md)
  A resource object that represents a player’s properties when you create a request.
- [object GameCenterMatchmakingTeamAssignment](gamecentermatchmakingteamassignment.md)
  The assignment of a player to a specific team during a Game Center matchmaking session.
- [object Location](location.md)
  A representation of a device location.
- [object Property](property.md)
  A representation of a game-specific property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingtestrequestinlinecreate)*