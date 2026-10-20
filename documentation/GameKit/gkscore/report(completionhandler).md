# report(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Reports a score to Game Center.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

*macOS, visionOS, watchOS*

```swift
func report(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
func report() async throws
```

```objc
- (void) reportScoreWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

The `value` property must be set before calling this method.

When this method is called, it creates a new background task to handle the request. The method then returns control to your game. Later, when the task is complete, GameKit calls your completion handler. The completion handler is always called on the main thread.

## Parameters

- `completionHandler`: A block to be called after the score is reported.

  The block receives the following parameter:

  - ***error***: If an error occurred, this parameter holds an error object that describes the problem. If the score was successfully reported, this parameter’s value is `nil`.

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
- [func issueChallenge(toPlayers: [String]?, message: String?)](./issuechallenge%28toplayers,message%29.md)
  Issues a score challenge to a set of players.
- [var playerID: String?](./playerid.md)
  The player identifier for the player that earned the score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(completionhandler:))*