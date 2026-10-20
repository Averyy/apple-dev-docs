# maxPlayers

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of players that can join the match.

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
var maxPlayers: Int { get set }
```

```objc
@property (assign) NSUInteger maxPlayers;
```

## Mentions

- [Finding multiple players for a game](../finding-multiple-players-for-a-game.md)
- [Finding players using matchmaking rules](../finding-players-using-matchmaking-rules.md)
- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The possible values range from the minimum number of players to the value returned by the [`maxPlayersAllowedForMatch(of:)`](./maxplayersallowedformatch%28of%29.md) method. To set the minimum number of players, use the [`minPlayers`](./minplayers.md) property.

If you use matchmaking rules, the rule set’s `maxPlayers` field constrains this value. Set this property to a value in the range of the rule set’s `minPlayers` and `maxPlayers` fields. The default value is the rule set’s `maxPlayers` field.

## See Also

### Related Documentation
- [Create a Rule Set](../../AppStoreConnectAPI/post-v1-gamecentermatchmakingrulesets.md)
  Create a rule set to contain matchmaking rules and teams.
### Restricting the number of players
- [class func maxPlayersAllowedForMatch(of: GKMatchType) -> Int](./maxplayersallowedformatch%28of%29.md)
  Returns the maximum number of players allowed in the match request for a given match type.
- [enum GKMatchType](../gkmatchtype.md)
  The kind of match managed by Game Center.
- [var minPlayers: Int](./minplayers.md)
  The minimum number of players that can join the match.
- [var defaultNumberOfPlayers: Int](./defaultnumberofplayers.md)
  The default number of players for the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/maxplayers)*