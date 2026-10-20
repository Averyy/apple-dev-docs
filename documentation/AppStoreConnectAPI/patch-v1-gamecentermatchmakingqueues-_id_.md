# Modify a Queue

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the properties of a specific queue.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the queue.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingQueueUpdateRequest`

## Responses

- `200` OK (`GameCenterMatchmakingQueueResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting queues
- [Create a Queue](./post-v1-gamecentermatchmakingqueues.md)
  Create a queue and add it to a rule set.
- [Delete a Queue](./delete-v1-gamecentermatchmakingqueues-_id_.md)
  Delete a specific queue in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecentermatchmakingqueues-_id_)*