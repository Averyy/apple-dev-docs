# Modify a Team

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific team in a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingTeams/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the team.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingTeamUpdateRequest`

## Responses

- `200` OK (`GameCenterMatchmakingTeamResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting teams
- [Create a Team](./post-v1-gamecentermatchmakingteams.md)
  Add a game-specific team to a rule set.
- [Delete a Team](./delete-v1-gamecentermatchmakingteams-_id_.md)
  Delete a game-specific team in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecentermatchmakingteams-_id_)*