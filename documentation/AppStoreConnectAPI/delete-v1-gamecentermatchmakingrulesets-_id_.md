# Delete a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a rule set along with its matchmaking rules and teams.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: A unique identifier for the rule set.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rule sets
- [Create a Rule Set](./post-v1-gamecentermatchmakingrulesets.md)
  Create a rule set to contain matchmaking rules and teams.
- [Modify a Rule Set](./patch-v1-gamecentermatchmakingrulesets-_id_.md)
  Update the attributes of a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecentermatchmakingrulesets-_id_)*