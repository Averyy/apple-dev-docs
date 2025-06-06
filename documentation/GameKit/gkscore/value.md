# value

**Framework**: GameKit  
**Kind**: property

The score earned by the player.

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
var value: Int64 { get set }
```

#### Discussion

You can use any algorithm you want to calculate scores in your game. Your game must set the `value` property before reporting a score, otherwise an error is returned.

The value provided by a score object is interpreted by Game Center only when formatted for display. You determine how your scores are formatted when you define the leaderboard in App Store Connect.

## See Also

- [var category: String?](gkscore/category.md)
  The leaderboard that this score belongs to.
- [var context: UInt64](gkscore/context.md)
  An integer value used by your game.
- [var date: Date](gkscore/date.md)
  The date and time when the score was earned.
- [var formattedValue: String?](gkscore/formattedvalue.md)
  Returns the player’s score as a localized string.
- [var leaderboardIdentifier: String](gkscore/leaderboardidentifier.md)
  The identifier for the leaderboard.
- [var player: GKPlayer](gkscore/player.md)
  The player who earned the score.
- [var rank: Int](gkscore/rank.md)
  The position of the score in the results of a leaderboard search.
- [var shouldSetDefaultLeaderboard: Bool](gkscore/shouldsetdefaultleaderboard.md)
  A Boolean value that indicates whether this score should also update the default leaderboard.
- [init(leaderboardIdentifier: String)](gkscore/init(leaderboardidentifier:).md)
  Returns an initialized score object using the local player and the current date.
- [init(leaderboardIdentifier: String, player: GKPlayer)](gkscore/init(leaderboardidentifier:player:).md)
  Returns an initialized score object for the specified leaderboard and player.
- [init(category: String?)](gkscore/init(category:).md)
  Returns an initialized score object.
- [init?(leaderboardIdentifier: String, forPlayer: String)](gkscore/init(leaderboardidentifier:forplayer:).md)
  Returns an initialized score object for the specified leaderboard and player.
- [func issueChallenge(toPlayers: [String]?, message: String?)](gkscore/issuechallenge(toplayers:message:).md)
  Issues a score challenge to a set of players.
- [var playerID: String?](gkscore/playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](gkscore/report(completionhandler:).md)
  Reports a score to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/value)*