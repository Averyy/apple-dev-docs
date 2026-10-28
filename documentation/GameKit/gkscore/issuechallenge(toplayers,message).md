# issueChallenge(toPlayers:message:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Issues a score challenge to a set of players.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func issueChallenge(toPlayers playerIDs: [String]?, message: String?)
```

```objc
- (void) issueChallengeToPlayers:(NSArray<NSString *> *) playerIDs message:(NSString *) message;
```

## Discussion

Set up your game to issue a challenge request only in direct response to a player action. That is, your game provides a user interface that allows the player to choose to issue a challenge and choose which friends receive the challenge, and only issue a challenge when the player wishes to do so.

## Parameters

- `playerIDs`: The identifiers for the players to challenge. Because Game Center limits the number of players in a challenge request to 10, the maximum size of this array is 10.
- `message`: A text message to display to the players.

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
- [init?(leaderboardIdentifier: String, forPlayer: String)](./init%28leaderboardidentifier,forplayer%29.md)
  Returns an initialized score object for the specified leaderboard and player.
- [var playerID: String?](./playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](./report%28completionhandler%29.md)
  Reports a score to Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/issuechallenge(toplayers:message:))*