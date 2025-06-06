# report(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Reports a score to Game Center.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func report() async throws
```

#### Discussion

The `value` property must be set before calling this method.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, GameKit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `completionHandler`: The block receives the following parameter:

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
- [var value: Int64](gkscore/value.md)
  The score earned by the player.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(completionhandler:))*