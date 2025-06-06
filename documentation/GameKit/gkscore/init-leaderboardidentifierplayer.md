# init(leaderboardIdentifier:player:)

**Framework**: GameKit  
**Kind**: init

Returns an initialized score object for the specified leaderboard and player.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(leaderboardIdentifier identifier: String, player: GKPlayer)
```

#### Return Value

An initialized score object, or `nil` if an error occurred.

#### Discussion

Your game explicitly allocates and initializes a score object using the designated player and current date when it needs to report a new score to Game Center.

## Parameters

- `identifier`: Identifies the leaderboard that the score is being sent to.
- `player`: The   object identifying the player who’s score is being initialized.

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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/init(leaderboardidentifier:player:))*