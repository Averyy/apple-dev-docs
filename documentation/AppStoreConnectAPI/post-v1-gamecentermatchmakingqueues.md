# Create a Queue

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a queue and add it to a rule set.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues
{
    “data”: {
        “type”: “gameCenterMatchmakingQueues”,
        “attributes”: {
            “referenceName”: “com.example.mygame.GameSettingsQueue”
        },
        “relationships”: {
            “ruleSet”: {
                “data”: {
                    “type”: “gameCenterMatchmakingRuleSets”,
                    “id”: “7353266e-8c6f-4cbe-8f0f-5108332a1146”
                }
            }
        }
    }
}
```

**Response**:

```json
{
    “data”: {
        “type”: “gameCenterMatchmakingQueues”,
        “id”: “aa1c1e6b-f8a9-4bad-b969-860dfd1485c5”,
        “attributes”: {
            “referenceName”: “com.example.mygame.GameSettingsQueue”
        },
        “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/aa1c1e6b-f8a9-4bad-b969-860dfd1485c5”
        }
    },
    “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues”
    }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingQueueCreateRequest`

## Responses

- `201` Created (`GameCenterMatchmakingQueueResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting queues
- [Modify a Queue](./patch-v1-gamecentermatchmakingqueues-_id_.md)
  Update the properties of a specific queue.
- [Delete a Queue](./delete-v1-gamecentermatchmakingqueues-_id_.md)
  Delete a specific queue in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecentermatchmakingqueues)*