# queueName

**Framework**: GameKit  
**Kind**: property

The name of the queue that Game Center places the match request in.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
var queueName: String? { get set }
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)
- [Assigning players to teams using rules](assigning-players-to-teams-using-rules.md)
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Finding players for custom server-based games](finding-players-for-custom-server-based-games.md)
- [Troubleshooting matchmaking rules using metrics](troubleshooting-matchmaking-rules-using-metrics.md)

#### Discussion

To use matchmaking rules, set the [`queueName`](gkmatchrequest/queuename.md) property to a queue name that you configure in App Store Connect. Then set [`properties`](gkmatchrequest/properties.md) and optionally [`recipientProperties`](gkmatchrequest/recipientproperties.md) to game-specific criteria.

A  is a uniform type identifier (UTI) that contains only alphanumeric characters (A-Z, a-z, 0-9), hyphens (-), or periods (.). The string should be in reverse-DNS format. Queue names are case sensitive.

Matchmaking rules evaluate the properties of match requests in the same queue to find the best match according to the rules that you set in App Store Connect for the queue. An error occurs if the queue doesn’t exist.

If this property is `nil`, Game Center doesn’t use matchmaking rules to find other players.

For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## See Also

- [Create a queue](../AppStoreConnectAPI/POST-v1-gameCenterMatchmakingQueues.md)
  Create a queue and add it to a rule set.
- [var properties: [String : Any]?](gkmatchrequest/properties.md)
  The criteria for the local player that Game Center uses to find other players when using matchmaking rules.
- [var recipientProperties: [GKPlayer : [String : Any]]?](gkmatchrequest/recipientproperties.md)
  The criteria for recipients of the match request that Game Center uses to find other players when using matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/queuename)*