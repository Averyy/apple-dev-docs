# GameCenterMatchmakingTeam

**Framework**: App Store Connect API  
**Kind**: dictionary

A team configuration within a Game Center matchmaking rule set, defining team size and composition rules.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingTeam
```

## Topics

### Objects
- [object GameCenterMatchmakingTeam.Attributes](gamecentermatchmakingteam/attributes-data.dictionary.md)
  The attributes of a game-specific team.

## Properties

- `attributes` (GameCenterMatchmakingTeam.Attributes): The attributes of the team.
- `id` (string) *(required)*: The unique identifier for the team.
- `links` (ResourceLinks): The link representations of the object.
- `type` (string) *(required)*: The type of resource object.

## See Also

- [object GameCenterMatchmakingTeamCreateRequest](gamecentermatchmakingteamcreaterequest.md)
  The request body you use to create a team.
- [object GameCenterMatchmakingTeamUpdateRequest](gamecentermatchmakingteamupdaterequest.md)
  The request body you use to modify a team.
- [object GameCenterMatchmakingTeamResponse](gamecentermatchmakingteamresponse.md)
  The response body for endpoints that create or modify a team.
- [object GameCenterMatchmakingTeamsResponse](gamecentermatchmakingteamsresponse.md)
  The response body for endpoints that get multiple teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingteam)*