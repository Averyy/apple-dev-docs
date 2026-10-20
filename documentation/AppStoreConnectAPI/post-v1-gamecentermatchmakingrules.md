# Create a Rule

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a matchmaking rule to a rule set.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules
{
    “data”: {
        “type”: “gameCenterMatchmakingRules”,
        “attributes”: {
            “type”: “COMPATIBLE”,
            “description”: “Check whether the players use the same game settings.”,
            “referenceName”: “SameTheme”,
            “expression”: “requests[0].properties.theme == requests[1].properties.theme”
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
        “type”: “gameCenterMatchmakingRules”,
        “id”: “2fd4bb73-3cca-46ca-aced-395c54ab11bc”,
        “attributes”: {
            “referenceName”: “SameTheme”,
            “description”: “Check whether the players use the same game settings.”,
            “type”: “COMPATIBLE”,
            “expression”: “requests[0].properties.theme == requests[1].properties.theme”,
            “weight”: null
        },
        “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules/2fd4bb73-3cca-46ca-aced-395c54ab11bc”
        }
    },
    “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules”
    }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterMatchmakingRuleCreateRequest`

## Responses

- `201` Created (`GameCenterMatchmakingRuleResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting rules
- [Modify a Rule](./patch-v1-gamecentermatchmakingrules-_id_.md)
  Update a specific matchmaking rule in a rule set.
- [Delete a Rule](./delete-v1-gamecentermatchmakingrules-_id_.md)
  Delete a matchmaking rule in a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecentermatchmakingrules)*