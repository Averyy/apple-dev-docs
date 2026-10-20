# Modify a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the attributes of a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: A unique identifier for the rule set.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingRuleSetUpdateRequest`

## Responses

- `200` OK (`GameCenterMatchmakingRuleSetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rule sets
- [Create a Rule Set](./post-v1-gamecentermatchmakingrulesets.md)
  Create a rule set to contain matchmaking rules and teams.
- [Delete a Rule Set](./delete-v1-gamecentermatchmakingrulesets-_id_.md)
  Delete a rule set along with its matchmaking rules and teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecentermatchmakingrulesets-_id_)*