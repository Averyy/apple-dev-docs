# properties

**Framework**: GameKit  
**Kind**: property

The criteria for the local player that Game Center uses to find other players when using matchmaking rules.

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
var properties: [String : Any]? { get set }
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)
- [Troubleshooting matchmaking rules using metrics](troubleshooting-matchmaking-rules-using-metrics.md)
- [Assigning players to teams using rules](assigning-players-to-teams-using-rules.md)
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Creating matchmaking rules for backward compatibility](creating-matchmaking-rules-for-backward-compatibility.md)
- [Letting players join matches using party codes](letting-players-join-matches-using-party-codes.md)

#### Discussion

Matchmaking rules may use one or more of these properties to improve matchmaking results and reduce wait times. You set rules in App Store Connect to find players that best match these properties in a reasonable amount of time by loosening the criteria over time.

This property contains key-value pairs where keys are strings with game-specific meanings, such as the skill level, game mode, play style, and other preferences. The keys can be any string, except `gc`, which GameKit reserves. The values need to be types that the [`JSONSerialization`](https://developer.apple.com/documentation/Foundation/JSONSerialization) class can convert to JSON data.

Set this property before you submit the match request to Game Center. For peer-to-peer matches, use the [`findMatch(for:withCompletionHandler:)`](gkmatchmaker/findmatch(for:withcompletionhandler:).md) method or present the [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) interface to submit a match request. For hosted matches, use the [`findMatchedPlayers(_:withCompletionHandler:)`](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md) method to include other player properties in the result.

```swift
// Create a match request.
let request = GKMatchRequest()

// Set the matchmaking rules queue name.
request.queueName = "com.example.mygame.PartyCodeQueue"

// Set properties to the game-specific keys you use in the rules.
request.properties = [ "partyCode": partyCode ]
```

If the [`queueName`](gkmatchrequest/queuename.md) property is `nil`, Game Center doesn’t use matchmaking rules and ignores the [`properties`](gkmatchrequest/properties.md) property.

For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## See Also

- [var queueName: String?](gkmatchrequest/queuename.md)
  The name of the queue that Game Center places the match request in.
- [var recipientProperties: [GKPlayer : [String : Any]]?](gkmatchrequest/recipientproperties.md)
  The criteria for recipients of the match request that Game Center uses to find other players when using matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/properties)*