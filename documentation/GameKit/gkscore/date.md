# date

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date and time when the score was earned.

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
var date: Date { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, readonly) NSDate * date;
```

*macOS*

```objc
@property (atomic, retain, readonly) NSDate * date;
```

#### Discussion

When you initialize the new score object, the `date` property is automatically set to the current date and time.

## See Also

### Deprecated Methods and Properties
- [var category: String?](./category.md)
  The leaderboard that this score belongs to.
- [var context: UInt64](./context.md)
  An integer value used by your game.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/date)*