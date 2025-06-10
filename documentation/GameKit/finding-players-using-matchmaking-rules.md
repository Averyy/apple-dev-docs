# Finding players using matchmaking rules

**Framework**: GameKit

Create a more customized and optimized gaming experience by using matchmaking rules to find players in a real-time game.

#### Overview

Matchmaking rules can improve the quality of matches, reduce wait times, and increase player retention by offering a more engaging and fair gaming experience. You create rules that customize the matchmaking criteria using your game-specific properties, such as rules that match players by skill level, game mode, geolocation, and language. You can also create rules that gradually loosen the matchmaking criteria over time to find matches more quickly.

Matchmaking rules contain compound expressions that Game Center applies to groups of match requests from players of your game. You write expressions using a JSON query language referencing game properties that you submit with the match request. You design the rules around the features of your game, group them into rule sets, and assign the rule sets to queues using the [`App Store Connect API`](https://developer.apple.com/documentation/AppStoreConnectAPI).

In your game code, you configure a match request to use matchmaking rules by setting its queue and game-specific properties. Then submit the match request using familiar GameKit APIs, and Game Center uses the matchmaking rules to find the best matches.

##### Create Rule Sets That Contain the Matchmaking Rules

A rule set is a collection of matchmaking rules for finding players in a multiplayer game. Use one or more rule sets to group matchmaking rules for the different configurations, levels, or other types of features in your game. You need to create at least one rule set before you can add matchmaking rules.

First decide on a format for the reference name that uniquely identifies rule sets in your organization. For example, use a reverse-domain name service path, such as `com.example.mygame.GameSettingsRules`.

Then decide on the minimum and maximum number of players allowed to join the matches. A valid match is any number of players between the minimum and maximum range, but Game Center assumes that more players provide a better experience, so looks for the maximum number of players first. The rule set’s `minPlayers` and `maxPlayers` fields constrain the [`GKMatchRequest`](gkmatchrequest.md) object’s [`minPlayers`](gkmatchrequest/minplayers.md) and [`maxPlayers`](gkmatchrequest/maxplayers.md) properties that you set in the code when you submit the match request.

Next, pass a [`GameCenterMatchmakingRuleSetCreateRequest.Data.Attributes`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingRuleSetCreateRequest/Data-data.dictionary/Attributes-data.dictionary) object — that contains the `referenceName`, `minPlayers`, and `maxPlayers` fields — to the [`Create a rule set`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRuleSets) endpoint.

```json
POST /v1/gameCenterMatchmakingRuleSets
{
    "data": {
        "type": "gameCenterMatchmakingRuleSets",
        "attributes": {
            "referenceName": "com.example.mygame.GameSettingsRuleSet",
            "ruleLanguageVersion": 1,
            "minPlayers": 2,
            "maxPlayers": 4
        },
        "relationships": {}
    }
}
```

Retain the `id` field of the [`GameCenterMatchmakingRuleSet`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingRuleSet) object that this endpoint returns; you need it to later add rules to this set.

```json
{
    "data": {
        "type": "gameCenterMatchmakingRuleSets",
        "id": "1fa9482d-12b5-48fc-9fb0-3c0ff16f605c",
        "attributes": {
            "referenceName": "com.example.mygame.GameSettingsRuleSet",
            "ruleLanguageVersion": 1,
            "minPlayers": 2,
            "maxPlayers": 4
        },
    ...
}
```

##### Add Matchmaking Rules to the Rule Sets

You add a rule to the rule set by passing the rule type, an expression, and a rule set, along with other settings, to the [`Create a rule`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRules) endpoint.

```json
POST /v1/gameCenterMatchmakingRules
{
    "data": {
        "type": "gameCenterMatchmakingRules",
        "attributes": {
            "type": "COMPATIBLE",
            "description": "Check whether the players use the same game settings.",
            "referenceName": "SameTheme",
            "expression": "requests[0].properties.theme == requests[1].properties.theme"
        },
        "relationships": {
            "ruleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "1fa9482d-12b5-48fc-9fb0-3c0ff16f605c"
                }
            }
        }
    }
}
```

In the `attributes` field, set the `type` field to either `COMPATIBLE`, `DISTANCE`, `MATCH`, or `TEAM`. Set the `description` and `referenceName` fields to strings that make sense for your game.

In the `relationships` field, set the `gameCenterRuleSet` field to the rule set that you want to add this rule to. Pass the `id` for the rule set in the [`GameCenterMatchmakingQueueCreateRequest.Data.Relationships.RuleSet.Data`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingQueueCreateRequest/Data-data.dictionary/Relationships-data.dictionary/RuleSet-data.dictionary/Data-data.dictionary) object.

Next write an expression for the rule that Game Center applies to two or more matches depending on the type.

##### Write Rich Expressions Using a Json Query Language

In the [`GameCenterMatchmakingRuleCreateRequest.Data.Attributes`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingRuleCreateRequest/Data-data.dictionary/Attributes-data.dictionary) object, set the `expression` field to an expression that returns either a Boolean or numeric value.

An expression is a [`JMESPath`](https://developer.apple.comhttps://jmespath.org) formatted string with Game Center matchmaking function additions. Game Center uses the expression as a query on a set of requests, depending on the type of rule and stage of the matchmaking algorithm, to find the most compatible players. The algorithm applies compatible rules first, distance rules next, followed by match and team rules.

If you set the `type` field to `COMPATIBLE`, the `requests` array in the expression contains two match requests. Use `requests[0]` to refer to the first one and `requests[1]` for the second one. For example, write an expression that returns [`true`](https://developer.apple.com/documentation/swift/true) if the theme game settings are the same.

```other
requests[0].properties.theme == requests[1].properties.theme
```

To loosen the matchmaking criteria over time, set the type to `MATCH` and use either the `agedAsSteppedValue()` or `agedValues()` function in an expression. These functions return different stepped values as the age of the requests in the queue increase.

For  more information on these functions, see [`Getting value based on age`](https://developer.apple.com/documentation/AppStoreConnectAPI/getting-value-based-on-age) and [`Getting value based on age using an array`](https://developer.apple.com/documentation/AppStoreConnectAPI/getting-value-based-on-age-using-an-array). For more information on the different types of rules and when Game Center applies the rules in the algorithm, see [`Expressions`](https://developer.apple.com/documentation/AppStoreConnectAPI/expressions) in App Store Connect API.

##### Configure a Queue for the Match Requests

You associate each rule set with a match request queue. Then Game Center applies the rules in the rule set to all active match requests in that queue.

Pass a reference name for the queue and a rule set to the [`Create a queue`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingQueues) endpoint. Set the `referenceName` field of the [`GameCenterMatchmakingQueueCreateRequest.Data.Attributes`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingQueueCreateRequest/Data-data.dictionary/Attributes-data.dictionary) object to a unique name in your organization, such as a string with a reverse-domain name prefix that is similar to your rule set reference names. Pass the `id` for the rule set in the [`GameCenterMatchmakingQueueCreateRequest.Data.Relationships.RuleSet.Data`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingQueueCreateRequest/Data-data.dictionary/Relationships-data.dictionary/RuleSet-data.dictionary/Data-data.dictionary) object.

```json
POST /v1/gameCenterMatchmakingQueues
{
    "data": {
        "type": "gameCenterMatchmakingQueues",
        "attributes": {
            "referenceName": "com.example.mygame.GameSettingsQueue"
        },
        "relationships": {
            "ruleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "1fa9482d-12b5-48fc-9fb0-3c0ff16f605c"
                }
            }
        }
    }
}
```

> ❗ **Important**:  If you have previous versions of your game that don’t use matchmaking rules, you can apply the same rules to match requests from those versions. Set the `classicMatchmakingBundleIds` field to the bundle IDs of the versions that you want to include when Game Center applies the rules. Otherwise, Game Center doesn’t match players running previous versions with current versions that specify a queue name. To create rules that include players running previous versions, see [`Creating matchmaking rules for backward compatibility`](creating-matchmaking-rules-for-backward-compatibility.md).

##### Create Match Requests That Use the Matchmaking Rules

In your code, create a [`GKMatchRequest`](gkmatchrequest.md) object and set the parameters of the game.

```swift
// Create a match request.
let request = GKMatchRequest()
```

To use matchmaking rules, set the [`queueName`](gkmatchrequest/queuename.md) property to the reference name of the queue that you previously created using the [`Create a queue`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingQueues) endpoint.

```swift
// Set the matchmaking rules queue name.
request.queueName = "com.example.mygame.GameSettingsQueue"
```

Set [`properties`](gkmatchrequest/properties.md) to a dictionary of key-value pairs that provide values for the local player’s game-specific properties that you can use in rule expressions. For example, add the local player’s preferred game configuration to properties.

```swift
// Set properties to the game-specific keys you use in the rules.
let theme = localPlayerData.theme
request.properties = [ "theme": theme]
```

If you set the matchmaking rule properties ([`queueName`](gkmatchrequest/queuename.md) and [`properties`](gkmatchrequest/properties.md)) of the [`GKMatchRequest`](gkmatchrequest.md) object, Game Center uses the rules in the rule set associated with the queue to find matches. When using matchmaking rules, Game Center ignores the subset that you specify using the [`playerGroup`](gkmatchrequest/playergroup.md) and [`playerAttributes`](gkmatchrequest/playerattributes.md) properties.

If you set the [`recipients`](gkmatchrequest/recipients.md) property to invite other players, you can also set their game-specific properties using the [`recipientProperties`](gkmatchrequest/recipientproperties.md) property.

##### Submit Match Requests to Game Center

You submit a match request using the same APIs regardless of whether you configure matchmaking rules. For example, present the [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) interface to enable players to invite others and automatch to fill empty spots.

```swift
// Present the interface where the player selects opponents and starts the game.
if let viewController = GKMatchmakerViewController(matchRequest: request) {
    viewController.matchmakerDelegate = self
    rootViewController?.present(viewController, animated: true) { }
}
```

If you can supply properties for recipients of a match request, then implement the [`matchmakerViewController(_:getMatchPropertiesForRecipient:withCompletionHandler:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:getmatchpropertiesforrecipient:withcompletionhandler:).md) protocol method to return the properties for each recipient that the local player selects in the interface.

When all the players accept their invitations and GameKit invokes the [`matchmakerViewController(_:didFind:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md) delegate method, you can implement it to access the properties for each player that you set when creating the requests.

For more information on the matchmaking flow after you submit a request, including when to accept invitations and start gameplay, see [`Finding multiple players for a game`](finding-multiple-players-for-a-game.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/finding-players-using-matchmaking-rules)*