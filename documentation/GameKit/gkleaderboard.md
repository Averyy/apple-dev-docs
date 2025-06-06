# GKLeaderboard

**Framework**: GameKit  
**Kind**: class

A leaderboard for a game that Game Center stores.

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
class GKLeaderboard
```

## Mentions

- [Creating recurring leaderboards](creating-recurring-leaderboards.md)

#### Overview

Leaderboards allow players to compare their scores against other players in your game. You configure a classic or recurring leaderboard in App Store Connect and then access the localized information for a leaderboard in your code using [`GKLeaderboard`](gkleaderboard.md) objects.

A  is persistent, that is, the scores never reset unless you delete the leaderboard. A  contains scores for a period of time useful for competitions and encouraging players to try for higher scores. You configure the duration, frequency, and delay between occurrences that Game Center uses to automatically restart the leaderboard in App Store Connect.

In your code, you use the identifier you set for the leaderboard in App Store Connect to submit scores or load leaderboards. Use the [`submitScore(_:context:player:leaderboardIDs:completionHandler:)`](gkleaderboard/submitscore(_:context:player:leaderboardids:completionhandler:).md) class method to submit a score to one or more leaderboards. Alternatively, load a recurring leaderboard using the [`loadLeaderboards(IDs:completionHandler:)`](gkleaderboard/loadleaderboards(ids:completionhandler:).md) class method and then submit a score using the [`submitScore(_:context:player:completionHandler:)`](gkleaderboard/submitscore(_:context:player:completionhandler:).md) method. To learn more about recurring leaderboards, see [`Creating recurring leaderboards`](creating-recurring-leaderboards.md).

To retrieve information about all leaderboards in your game, use the [`loadLeaderboards(IDs:completionHandler:)`](gkleaderboard/loadleaderboards(ids:completionhandler:).md) class method. To fetch the scores for a leaderboard, use the [`loadEntries(for:timeScope:range:completionHandler:)`](gkleaderboard/loadentries(for:timescope:range:completionhandler:).md) or [`loadEntries(for:timeScope:completionHandler:)`](gkleaderboard/loadentries(for:timescope:completionhandler:).md) method. Use the parameters of these methods to filter the scores to the player’s friends, a rank, and time period when the score occurs.

You must create leaderboard objects using one of the load methods above. If the request is successful, GameKit passes corresponding [`GKLeaderboard`](gkleaderboard.md) objects to the handler. GameKit doesn’t load the images you add to App Store Connect when it loads the leaderboards. Use the [`loadImage(completionHandler:)`](gkleaderboard/loadimage(completionhandler:).md) method to get the image for a leaderboard.

## Topics

### Accessing Identifier and Type Properties
- [var baseLeaderboardID: String](gkleaderboard/baseleaderboardid.md)
  The ID that Game Center uses to identify this leaderboard.
- [var title: String?](gkleaderboard/title.md)
  The localized title for the leaderboard.
- [var type: GKLeaderboard.LeaderboardType](gkleaderboard/type.md)
  The type of leaderboard, classic or recurring.
- [GKLeaderboard.LeaderboardType](gkleaderboard/leaderboardtype.md)
  Specifies whether a leaderboard is recurring.
- [var groupIdentifier: String?](gkleaderboard/groupidentifier.md)
  The identifier for the group the leaderboard belongs to.
### Accessing Recurring Leaderboard Properties
- [var startDate: Date?](gkleaderboard/startdate.md)
  The date and time a recurring leaderboard occurrence starts accepting scores.
- [var nextStartDate: Date?](gkleaderboard/nextstartdate.md)
  The date and time the next recurring leaderboard occurrence starts accepting scores.
- [var duration: TimeInterval](gkleaderboard/duration.md)
  The duration from the start date that a recurring leaderboard occurrence accepts scores.
### Loading Leaderboards
- [class func loadLeaderboards(IDs: [String]?, completionHandler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkleaderboard/loadleaderboards(ids:completionhandler:).md)
  Loads leaderboards for the specified leaderboard IDs that Game Center uses.
- [func loadPreviousOccurrence(completionHandler: (GKLeaderboard?, (any Error)?) -> Void)](gkleaderboard/loadpreviousoccurrence(completionhandler:).md)
  Loads the previous recurring leaderboard occurrence that the player submits a score to.
### Loading Leaderboard Images
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkleaderboard/loadimage(completionhandler:).md)
  Loads the image for the leaderboard.
### Submitting Scores
- [class func submitScore(Int, context: Int, player: GKPlayer, leaderboardIDs: [String], completionHandler: ((any Error)?) -> Void)](gkleaderboard/submitscore(_:context:player:leaderboardids:completionhandler:).md)
  Submits a score to multiple leaderboards.
- [func submitScore(Int, context: Int, player: GKPlayer, completionHandler: ((any Error)?) -> Void)](gkleaderboard/submitscore(_:context:player:completionhandler:).md)
  Submits a score to the leaderboard.
### Loading Scores
- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:range:completionhandler:).md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:completionhandler:).md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.enum.md)
  Specifies the time period for filtering data.
- [GKLeaderboard.Entry](gkleaderboard/entry.md)
  Information about a single score by a player on a leaderboard.
### Deprecated
- [Deprecated symbols](gkleaderboard-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)
  Let players measure their own progress and compare their skills with friends and others.
- [Creating recurring leaderboards](creating-recurring-leaderboards.md)
  Create a leaderboard for your game that ranks player scores based on a schedule.
- [Adding Recurring Leaderboards to Your Game](adding-recurring-leaderboards-to-your-game.md)
  Encourage competition in your games by adding leaderboards that have a duration and repeat.
- [class GKLeaderboardSet](gkleaderboardset.md)
  Organizes leaderboards into logical and coherent groups.
- [class GKLeaderboardScore](gkleaderboardscore.md)
  Information about a player’s score on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard)*