# shouldSetDefaultLeaderboard

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this score should also update the default leaderboard.

**Availability**:
- iOS 5.0+ - Deprecated in 14.0
- iPadOS 5.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

## Declaration

```swift
var shouldSetDefaultLeaderboard: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL shouldSetDefaultLeaderboard;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), when the score is reported to Game Center, Game Center also updates the local player’s default leaderboard to match the value stored in the [`leaderboardIdentifier`](./leaderboardidentifier.md) property of the score object. This matches the behavior of the [`GKLeaderboard`](../gkleaderboard.md) class’s [`setDefault(_:withCompletionHandler:)`](../gkleaderboard/setdefault%28_,withcompletionhandler%29.md) class method. If the value of this property is [`false`](../../Swift/false.md), the default leaderboard is not changed by reporting the score. The default value of this property is [`false`](../../Swift/false.md).

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
- [var rank: Int](./rank.md)
  The position of the score in the results of a leaderboard search.
- [var value: Int64](./value.md)
  The score earned by the player.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/shouldsetdefaultleaderboard)*