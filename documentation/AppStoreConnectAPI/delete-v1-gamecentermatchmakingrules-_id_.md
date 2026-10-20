# Delete a Rule

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a matchmaking rule in a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: A unique identifier for the rule.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rules
- [Create a Rule](./post-v1-gamecentermatchmakingrules.md)
  Add a matchmaking rule to a rule set.
- [Modify a Rule](./patch-v1-gamecentermatchmakingrules-_id_.md)
  Update a specific matchmaking rule in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecentermatchmakingrules-_id_)*