# minPlayers

**Framework**: GameKit  
**Kind**: property

The minimum number of players that can join the match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var minPlayers: Int { get set }
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

The possible values range from `2` to the value returned by the [`maxPlayersAllowedForMatch(of:)`](gkmatchrequest/maxplayersallowedformatch(of:).md) method. To set the maximum number of players, use the [`maxPlayers`](gkmatchrequest/maxplayers.md) property.

If you use matchmaking rules, the rule set’s `minPlayers` field constrains this value. Set this property to a value in the range of the rule set’s `minPlayers` and `maxPlayers` fields. The default value is the rule set’s `minPlayers` field.

## See Also

- [Create a rule set](../AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRuleSets.md)
  Create a rule set to contain matchmaking rules and teams.
- [class func maxPlayersAllowedForMatch(of: GKMatchType) -> Int](gkmatchrequest/maxplayersallowedformatch(of:).md)
  Returns the maximum number of players allowed in the match request for a given match type.
- [enum GKMatchType](gkmatchtype.md)
  The kind of match managed by Game Center.
- [var maxPlayers: Int](gkmatchrequest/maxplayers.md)
  The maximum number of players that can join the match.
- [var defaultNumberOfPlayers: Int](gkmatchrequest/defaultnumberofplayers.md)
  The default number of players for the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/minplayers)*