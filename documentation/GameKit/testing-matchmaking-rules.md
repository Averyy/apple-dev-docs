# Testing matchmaking rules

**Framework**: GameKit

Test your matchmaking rules before you use them in your game.

#### Overview

Before you write any code, you can test your matchmaking rules on the server side to ensure that they find compatible players without long wait times. You pass the rule set and sample match requests to the test API, and it responds with the match results.

To download a script that helps test your matchmaking rules, see [`Testing matchmaking rules using a Python script`](https://developer.apple.comhttps://github.com/apple/game-center-tools). For examples using the script, see [`Meet rule-based matchmaking in Game Center`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111376/).

##### Create Sample Match Requests

Create an array of [`GameCenterMatchmakingTestRequestInlineCreate`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingTestRequestInlineCreate) objects that represent sample match requests. Set the `type` field to `gameCenterMatchmakingTestRequests` and the `id` field to a unique identifier for the match request.

The `attributes` field has the same fields as the `Request` object that you use in expressions. Set the required `requestName` field to a unique string and the `bundleId` field to your game’s bundle identifier. Set the `platform` and `appVersion` fields to appropriate values, such as `1.0` and `IOS`. Set the `secondsInQueue` field to `0` unless you want to test rules with different match request ages.

```json
"included": [
        {
            "type": "gameCenterMatchmakingTestRequests",
            "id": "${r1}",
            "attributes": {
                "requestName": "r1",
                "appVersion": "1.0.0",
                "bundleId": "com.example.mygame",
                "platform": "IOS",
                "secondsInQueue": 0
            },
            "relationships": {
                "matchmakingPlayerProperties": {
                    "data": [
                        {
                            "type": "gameCenterMatchmakingTestPlayerProperties",
                            "id": "${r1_p1}"
                        }
                    ]
                }
            }
        },
        {
            "type": "gameCenterMatchmakingTestRequests",
            "id": "${r2}",
            "attributes": {
                "requestName": "r2",
                "appVersion": "1.0.0",
                "bundleId": "com.example.mygame",
                "platform": "IOS",
                "secondsInQueue": 0
            },
            "relationships": {
                "matchmakingPlayerProperties": {
                    "data": [
                        {
                            "type": "gameCenterMatchmakingTestPlayerProperties",
                            "id": "${r2_p1}"
                        }
                    ]
                }
            }
        },
...
```

In the `relationships` field, include resource objects for any game-specific properties that you use in the expressions. For example, if you’re testing party code rules, described in [`Letting players join matches using party codes`](letting-players-join-matches-using-party-codes.md), add a [`GameCenterMatchmakingTestRequestInlineCreate.Relationships.MatchmakingPlayerProperties`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingTestRequestInlineCreate/Relationships-data.dictionary/MatchmakingPlayerProperties-data.dictionary) object to each match request.

Then append a corresponding [`GameCenterMatchmakingTestPlayerPropertyInlineCreate`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingTestPlayerPropertyInlineCreate) object for each of the match request. In the `attributes` field, provide a key-value pair for each property, such as the `partyCode` property.

```json
...
        {
            "type": "gameCenterMatchmakingTestPlayerProperties",
            "id": "${r1_p1}",
            "attributes": {
                "properties": [
                    {
                        "key": "partyCode",
                        "value": "\"Q1R5A6T9\""
                    }
                ],
                "playerId": "r1_p1"
            }
        },
        {
            "type": "gameCenterMatchmakingTestPlayerProperties",
            "id": "${r2_p1}",
            "attributes": {
                "properties": [
                    {
                        "key": "partyCode",
                        "value": "\"Q1R5A6T9\""
                    }
                ],
                "playerId": "r2_p1"
            }
        }
    ]
}
```

##### Test the Matchmaking Rules

Apply the matchmaking rules by passing the associated rule set and the sample match requests to the [`Test a rule set`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRuleSetTests) endpoint. Pass the rule set `id` using the `matchmakingRuleSet` field and pass resource objects representing the match requests in the `matchmakingRequests` field. Then pass the array of [`GameCenterMatchmakingTestRequestInlineCreate`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingTestRequestInlineCreate) and [`GameCenterMatchmakingTestPlayerPropertyInlineCreate`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingTestPlayerPropertyInlineCreate) objects, that you create above, in the `included` field.

```json
POST /v1/gameCenterMatchmakingRuleSetTests
{
    "data": {
        "type": "gameCenterMatchmakingRuleSetTests",
        "attributes": {},
        "relationships": {
            "matchmakingRuleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "9e313753-2b8a-4762-b941-26f30c4184d2"
                }
            },
            "matchmakingRequests": {
                "data": [
                    {
                        "type": "gameCenterMatchmakingTestRequests",
                        "id": "${r1}"
                    },
                    {
                        "type": "gameCenterMatchmakingTestRequests",
                        "id": "${r2}"
                    }
                ]
            }
        }
    },
    "included": [...}
}
```

The endpoint response contains the matchmaking results. Parse the `matchmakingResults` array in the [`GameCenterMatchmakingRuleSetTest.Attributes`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingRuleSetTest/Attributes-data.dictionary) object. If the rule set contains team rules, the team assignments appear in the `teamAssignments` field of the [`GameCenterMatchmakingRuleSetTest.Attributes.MatchmakingResults`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingRuleSetTest/Attributes-data.dictionary/MatchmakingResults-data.dictionary) object.

```json
{
    "data": {
        "type": "gameCenterMatchmakingRuleSetTests",
        "attributes": {
            "matchmakingResults": [
                [
                    {
                        "requestName": "r1",
                        "teamAssignments": null
                    },
                    {
                        "requestName": "r2",
                        "teamAssignments": null
                    }
                ]
            ]
        },
...
```

To create a rule set, see [`Create rule sets that contain the matchmaking rules`](finding-players-using-matchmaking-rules#Create-rule-sets-that-contain-the-matchmaking-rules.md), and to create team rules, see [`Assigning players to teams using rules`](assigning-players-to-teams-using-rules.md).

## See Also

- [Troubleshooting matchmaking rules using metrics](troubleshooting-matchmaking-rules-using-metrics.md)
  Investigate issues with Game Center by evaluating your matchmaking rules using metrics endpoints.
- [Testing rule sets with player traffic using metrics](testing-rule-sets-with-player-traffic-using-metrics.md)
  Get metrics on a new rule set with real match requests before releasing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/testing-matchmaking-rules)*