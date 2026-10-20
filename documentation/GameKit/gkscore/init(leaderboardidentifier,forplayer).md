# init(leaderboardIdentifier:forPlayer:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized score object for the specified leaderboard and player.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
init?(leaderboardIdentifier identifier: String, forPlayer playerID: String)
```

```objc
- (instancetype) initWithLeaderboardIdentifier:(NSString *) identifier forPlayer:(NSString *) playerID;
```

#### Return Value

An initialized score object, or `nil` if an error occurred.

#### Discussion

Your game explicitly allocates and initializes a score object using the designated player and current date when it needs to report a new score to Game Center.

## Parameters

- `identifier`: Identifies the leaderboard that the score is being sent to.
- `playerID`: The identifier of the player who’s score is being initialized.

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
- [var shouldSetDefaultLeaderboard: Bool](./shouldsetdefaultleaderboard.md)
  A Boolean value that indicates whether this score should also update the default leaderboard.
- [init(leaderboardIdentifier: String)](./init%28leaderboardidentifier%29.md)
  Returns an initialized score object using the local player and the current date.
- [init(leaderboardIdentifier: String, player: GKPlayer)](./init%28leaderboardidentifier,player%29.md)
  Returns an initialized score object for the specified leaderboard and player.
- [init(category: String?)](./init%28category%29.md)
  Returns an initialized score object.
- [func issueChallenge(toPlayers: [String]?, message: String?)](./issuechallenge%28toplayers,message%29.md)
  Issues a score challenge to a set of players.
- [var playerID: String?](./playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](./report%28completionhandler%29.md)
  Reports a score to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/init(leaderboardidentifier:forplayer:))*