# Create a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a rule set to contain matchmaking rules and teams.

**Availability**:
- App Store Connect API 3.1+

## Discussion

### Example Request and Response

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1//gameCenterMatchmakingRuleSets
{
    “data”: {
        “type”: “gameCenterMatchmakingRuleSets”,
        “attributes”: {
            “referenceName”: “com.example.mygame.GameSettingsRuleSet”,
            “ruleLanguageVersion”: 1,
            “minPlayers”: 2,
            “maxPlayers”: 4
        },
        “relationships”: {}
    }
}
```

**Response**:

```json
{
    “data”: {
        “type”: “gameCenterMatchmakingRuleSets”,
        “id”: “7353266e-8c6f-4cbe-8f0f-5108332a1146”,
        “attributes”: {
            “referenceName”: “com.example.mygame.GameSettingsRuleSet”,
            “ruleLanguageVersion”: 1,
            “minPlayers”: 2,
            “maxPlayers”: 4
        },
        “relationships”: {
            “teams”: {
                “links”: {
                    “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/relationships/teams”,
                    “related”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/teams”
                }
            },
            “rules”: {
                “links”: {
                    “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/relationships/rules”,
                    “related”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/rules”
                }
            },
            “matchmakingQueues”: {
                “links”: {
                    “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/relationships/matchmakingQueues”,
                    “related”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146/matchmakingQueues”
                }
            }
        },
        “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/7353266e-8c6f-4cbe-8f0f-5108332a1146”
        }
    },
    “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets”
    }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingRuleSetCreateRequest`

## Responses

- `201` Created (`GameCenterMatchmakingRuleSetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rule sets
- [Modify a Rule Set](./patch-v1-gamecentermatchmakingrulesets-_id_.md)
  Update the attributes of a rule set.
- [Delete a Rule Set](./delete-v1-gamecentermatchmakingrulesets-_id_.md)
  Delete a rule set along with its matchmaking rules and teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecentermatchmakingrulesets)*