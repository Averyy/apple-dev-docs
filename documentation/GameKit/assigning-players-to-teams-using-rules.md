# Assigning players to teams using rules

**Framework**: GameKit

Set criteria for assigning players to teams in your game using matchmaking rules.

#### Overview

If your game has teams, add team rules to balance the assignment of players to teams that makes gameplay more fair and enjoyable for the players. Team rules create constraints on adding players to teams.

Game Center applies the team rules to match requests in the queue after applying other compatible, distance, and match rules. Game Center applies the team rules to candidate teams from combinations of compatible match requests.

Before you begin adding team rules:

- Create a rule set to contain the team rules using the [`Create a rule set`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRuleSets) endpoint.
- Add compatibility and distance rules that filter the match requests using the [`Create a rule`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRules) endpoint.
- Add match rules, such as skill-level rules, that apply to compatible requests.

For more information on creating the other types of rules, see [`Letting players join matches using party codes`](letting-players-join-matches-using-party-codes.md) and [`Finding players with similar skill levels`](finding-players-with-similar-skill-levels.md).

##### Add Teams to the Rule Set

Create two or more teams to compete in your game using the [`Create a team`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingTeams) endpoint.

In the attributes property, pass the minimum and maximum players, and a name of the team. In the relationships property, pass the rule set `id` that the [`Create a rule set`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRuleSets) endpoint returns in the response.

```json
POST /v1/gameCenterMatchmakingTeams
{
    "data": {
        "type": "gameCenterMatchmakingTeams",
        "attributes": {
            "minPlayers": 2,
            "maxPlayers": 4,
            "referenceName": "blue"
        },
        "relationships": {
            "ruleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "6195839b-4ef7-4798-b91d-d59802111607"
                }
            }
        }
    }
}
```

Create one or more other teams to compete with the first team using a different name and add them to the same rule set:

```json
POST /v1/gameCenterMatchmakingTeams
{
    "data": {
        "type": "gameCenterMatchmakingTeams",
        "attributes": {
            "minPlayers": 2,
            "maxPlayers": 4,
            "referenceName": "red"
        },
        "relationships": {
            "ruleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "6195839b-4ef7-4798-b91d-d59802111607"
                }
            }
        }
    }
}
```

##### Add Team Rules to the Rule Set

You can add one or more team rules to your rule set depending on how many constraints you want to add to the team assignments. For example, if your matches have a variable number of team members, you can create a team rule that keeps the sizes of the teams balanced. You can also balance the teams by skill level and ensure that invited players are on the same team.

To create a team rule, set the rule’s type field to `TEAM` and the `teams` array becomes available to use in expressions. The `teams` array contains `Team` objects that represent the teams in the rule set. A team has a `players` property that contains `Player` objects that represent the players assigned to the team.

Write an expression that returns [`true`](https://developer.apple.com/documentation/swift/true) when the size of the teams are the same using expression functions, the `teams` array, and the `players` property.

```json
length(teams[?name == 'red'].players[]) == length(teams[?name == 'blue'].players[])
```

Pass the rule type, the expression, and the rule set, along with other settings, to the [`Create a rule`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRules) endpoint.

```json
POST /v1/gameCenterMatchmakingRules
{
    "data": {
        "type": "gameCenterMatchmakingRules",
        "attributes": {
            "type": "TEAM",
            "description": "Teams must have same number of players",
            "referenceName": "SameSizeTeams",
            "expression": "length(teams[?name == 'red'].players[]) == length(teams[?name == 'blue'].players[])"
        },
        "relationships": {
            "ruleSet": {
                "data": {
                    "type": "gameCenterMatchmakingRuleSets",
                    "id": "6195839b-4ef7-4798-b91d-d59802111607"
                }
            }
        }
    }
}
```

In team rule expressions, the [`Player`](https://developer.apple.com/documentation/AppStoreConnectAPI/player) object has a `requestName` field that is an identifier for the associated match request. For more information on the [`Team`](https://developer.apple.com/documentation/AppStoreConnectAPI/team) and [`Player`](https://developer.apple.com/documentation/AppStoreConnectAPI/player) objects you use in team rules, see [`Expressions`](https://developer.apple.com/documentation/AppStoreConnectAPI/expressions) in App Store Connect API.

##### Create Match Requests That Assign Players to Teams

In your code, create a [`GKMatchRequest`](gkmatchrequest.md) object that initiates a team game. Set the [`queueName`](gkmatchrequest/queuename.md) property to the reference name of the queue that contains your team rules.

```swift
// Create a match request.
let request = GKMatchRequest()

// Set the matchmaking rules queue name.
request.queueName = "com.example.mygame.TeamBasedQueue"
```

If you add a rule to balance the teams by skill level, add the local player’s skill to the [`properties`](gkmatchrequest/properties.md) property:

```swift
// Set properties to the game-specific keys you use in the rules.
let skill = localPlayerData.skill
request.properties = [ "skill": skill]
```

Game Center finds all compatible players and assigns them to teams.

##### Get Team Assignments When Players Accept Invitations

When all the players accept their invitations, GameKit invokes the `GKMatchmakerViewControllerDelegate` [`matchmakerViewController(_:didFind:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md) method in the app instances for all players in the game, including the player who sent the invitations.

```swift
func matchmakerViewController(_ viewController: GKMatchmakerViewController,
                                  didFind match: GKMatch) {
    // Dismiss the view controller.
    viewController.dismiss(animated: true, completion: nil)

    // Set the match delegate.
    match.delegate = myGame
          
    // Start the game with the players in the match.
}
```

Before your implementation of this delegate method starts the game, you can get all the team assignments from the [`GKMatch`](gkmatch.md) object. Use the [`players`](gkmatch/players.md) property to get the players that accepted the invitation, including the player that initiated the match. Then use the `GKMatch.``playersProperties` to get the game-specific properties for each player, such as the `skill` property, including the team assignment. If you add team rules to your rule set, use the `gc` and `team` keys to get the name of the player’s team that you previously configured using the [`Create a team`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingTeams) endpoint.

```swift
// Get the local player's team assignment.
properties = match.properties
team = properties["gc"]["team"]
```

## See Also

- [Letting players join matches using party codes](letting-players-join-matches-using-party-codes.md)
  Add a rule that lets players invite players and join matches using a shared party code.
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)
  Add a rule to find players in a range of skill levels to balance competitive gameplay.
- [Creating matchmaking rules for backward compatibility](creating-matchmaking-rules-for-backward-compatibility.md)
  Add matchmaking rules that support previous classic matchmaking versions of your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/assigning-players-to-teams-using-rules)*