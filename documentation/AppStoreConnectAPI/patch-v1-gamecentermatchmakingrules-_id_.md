# Modify a Rule

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific matchmaking rule in a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the rule.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingRuleUpdateRequest`

## Responses

- `200` OK (`GameCenterMatchmakingRuleResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rules
- [Create a Rule](./post-v1-gamecentermatchmakingrules.md)
  Add a matchmaking rule to a rule set.
- [Delete a Rule](./delete-v1-gamecentermatchmakingrules-_id_.md)
  Delete a matchmaking rule in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecentermatchmakingrules-_id_)*