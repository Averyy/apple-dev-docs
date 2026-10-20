# rank

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The position of the score in the results of a leaderboard search.

**Availability**:
- iOS 4.1+ - Deprecated in 14.0
- iPadOS 4.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

## Declaration

```swift
var rank: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) NSInteger rank;
```

*macOS*

```objc
@property (atomic, assign, readonly) NSInteger rank;
```

#### Discussion

The value of this property is only valid on score objects returned from Game Center. The `rank` property represents the position of the score in the returned results, with `1` being the best score, `2` being the second best, and so on.

## See Also

### Deprecated Methods and Properties
- [var category: String?](./category.md)
  The leaderboard that this score belongs to.
- [var context: UInt64](./context.md)
  An integer value used by your game.
- [var date: Date](./date.md)
  The date and time when the score was earned.
- [var formattedValue: String?](./formattedvalue.md)
  Returns the player’s score as a localized string.
- [var leaderboardIdentifier: String](./leaderboardidentifier.md)
  The identifier for the leaderboard.
- [var player: GKPlayer](./player.md)
  The player who earned the score.
- [var value: Int64](./value.md)
  The score earned by the player.
- [var shouldSetDefaultLeaderboard: Bool](./shouldsetdefaultleaderboard.md)
  A Boolean value that indicates whether this score should also update the default leaderboard.
- [init(leaderboardIdentifier: String)](./init%28leaderboardidentifier%29.md)
  Returns an initialized score object using the local player and the current date.
- [init(leaderboardIdentifier: String, player: GKPlayer)](./init%28leaderboardidentifier,player%29.md)
  Returns an initialized score object for the specified leaderboard and player.
- [init(category: String?)](./init%28category%29.md)
  Returns an initialized score object.
- [init?(leaderboardIdentifier: String, forPlayer: String)](./init%28leaderboardidentifier,forplayer%29.md)
  Returns an initialized score object for the specified leaderboard and player.
- [func issueChallenge(toPlayers: [String]?, message: String?)](./issuechallenge%28toplayers,message%29.md)
  Issues a score challenge to a set of players.
- [var playerID: String?](./playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](./report%28completionhandler%29.md)
  Reports a score to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/rank)*