# GKLeaderboardSet

**Framework**: GameKit  
**Kind**: class

Organizes leaderboards into logical and coherent groups.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKLeaderboardSet
```

#### Overview

A [`GKLeaderboardSet`](gkleaderboardset.md) object represents a group of leaderboards that you configure in App Store Connect. For example, if your game has different worlds or levels, you can organize the leaderboards into sets for each world or level. In the Game Center dashboard, players navigate from the leaderboard sets to the individual leaderboards. If you use leaderboard sets, you must have one or more leaderboards and then place each leaderboard in a set, which can be a mix of classic and recurring leaderboards.

To load all the leaderboard sets for your game, use the [`loadLeaderboardSets(completionHandler:)`](gkleaderboardset/loadleaderboardsets(completionhandler:).md) class method. Then use the `title`, `identifier`, and `groupIdentifier` properties to access the data for each leaderboard set. If you localize the leaderboard set in App Store Connect, the `title` property localizes. GameKit only sets the `groupIdentifier` property when your game is in a game group. To load the images you add to App Store Connect for each set, use the [`loadImage(completionHandler:)`](gkleaderboardset/loadimage(completionhandler:).md) method. Then use the [`loadLeaderboards(handler:)`](gkleaderboardset/loadleaderboards(handler:).md) method to get the leaderboards in each set.

To organize leaderboards into sets, see [`Configure leaderboard sets`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboard-sets) in App Store Connect Help.

## Topics

### Accessing Properties
- [var title: String](gkleaderboardset/title.md)
  The localized title for the leaderboard set.
- [var identifier: String?](gkleaderboardset/identifier.md)
  The identifier for the leaderboard set.
- [var groupIdentifier: String?](gkleaderboardset/groupidentifier.md)
  The identifier for the group that the leaderboard set belongs to.
### Loading Leaderboard Sets
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkleaderboardset/loadimage(completionhandler:).md)
  Loads the localized image that you associate with the leaderboard set.
- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboardsets(completionhandler:).md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkleaderboardset/loadleaderboards(handler:).md)
  Loads the leaderboards in the leaderboard set.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboards(completionhandler:).md)
  Loads all of the leaderboards for the current leaderboard set.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)
  Let players measure their own progress and compare their skills with friends and others.
- [Creating recurring leaderboards](creating-recurring-leaderboards.md)
  Create a leaderboard for your game that ranks player scores based on a schedule.
- [Adding Recurring Leaderboards to Your Game](adding-recurring-leaderboards-to-your-game.md)
  Encourage competition in your games by adding leaderboards that have a duration and repeat.
- [class GKLeaderboard](gkleaderboard.md)
  A leaderboard for a game that Game Center stores.
- [class GKLeaderboardScore](gkleaderboardscore.md)
  Information about a player’s score on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset)*