# GKNotificationBanner

**Framework**: GameKit  
**Kind**: class

A Game Center-style banner that displays a message to the local player.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKNotificationBanner
```

#### Overview

This class displays a message in a banner to the local player, similar to the banner that GameKit displays when a player earns an achievement. If the game is in the foreground, the banner appears immediately. If the game is in the background, the banner appears when the game becomes active.

To display the banner with your message, use the [`show(withTitle:message:completionHandler:)`](gknotificationbanner/show(withtitle:message:completionhandler:).md) method. To specify a duration that GameKit presents the banner, use the [`show(withTitle:message:duration:completionHandler:)`](gknotificationbanner/show(withtitle:message:duration:completionhandler:).md) method instead. Optionally, pass these methods a completion handler that GameKit calls after it dismisses the banner.

```swift
GKNotificationBanner.show(withTitle:"Hooray",
                          message:"You passed level 1 and can move to level 2.",
                          completionHandler: nil)
```

## Topics

### Displaying the Banner
- [class func show(withTitle: String?, message: String?, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:completionhandler:).md)
  Displays a banner with a title and message to the player.
- [class func show(withTitle: String?, message: String?, duration: TimeInterval, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:duration:completionhandler:).md)
  Displays a banner to the player for a specified period of time.

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

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKChallenge](gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gknotificationbanner)*