# init(category:)

**Framework**: GameKit  
**Kind**: init

Returns an initialized score object.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(category: String?)
```

#### Return Value

An initialized score object, or `nil` if an error occurred.

#### Discussion

Your game explicitly allocates and initializes a score object when it needs to report a new score to Game Center.

## Parameters

- `category`: An identifier for a specific leaderboard you’ve configured in App Store Connect. Must not be  .

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
- [init?(leaderboardIdentifier: String, forPlayer: String)](gkscore/init(leaderboardidentifier:forplayer:).md)
  Returns an initialized score object for the specified leaderboard and player.
- [func issueChallenge(toPlayers: [String]?, message: String?)](gkscore/issuechallenge(toplayers:message:).md)
  Issues a score challenge to a set of players.
- [var playerID: String?](gkscore/playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](gkscore/report(completionhandler:).md)
  Reports a score to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/init(category:))*