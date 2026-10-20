# Create a Team

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a game-specific team to a rule set.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingTeams
{
    “data”: {
        “type”: “gameCenterMatchmakingTeams”,
        “attributes”: {
            “minPlayers”: 2,
            “maxPlayers”: 4,
            “referenceName”: “blue”
        },
        “relationships”: {
            “ruleSet”: {
                “data”: {
                    “type”: “gameCenterMatchmakingRuleSets”,
                    “id”: “50d7eed2-8016-441a-a919-db3d863f433c”
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
        “type”: “gameCenterMatchmakingTeams”,
        “id”: “2a68632b-0129-4c07-8e84-6da57a76499d”,
        “attributes”: {
            “referenceName”: “blue”,
            “minPlayers”: 2,
            “maxPlayers”: 4
        },
        “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingTeams/2a68632b-0129-4c07-8e84-6da57a76499d”
        }
    },
    “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingTeams”
    }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingTeams`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingTeamCreateRequest`

## Responses

- `201` Created (`GameCenterMatchmakingTeamResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting teams
- [Modify a Team](./patch-v1-gamecentermatchmakingteams-_id_.md)
  Update a specific team in a rule set.
- [Delete a Team](./delete-v1-gamecentermatchmakingteams-_id_.md)
  Delete a game-specific team in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecentermatchmakingteams)*