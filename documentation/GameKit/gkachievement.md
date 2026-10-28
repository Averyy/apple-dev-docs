# GKAchievement

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

An achievement you can award a player as they make progress toward and reach a goal in your game.

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
class GKAchievement
```

```objc
@interface GKAchievement : NSObject
```

## Mentions

- [Rewarding players with achievements](./rewarding-players-with-achievements.md)

## Overview

Before using this class, configure your game achievements in App Store Connect. Then the dashboard shows the achievements initially locked and you can access them in your code.

Use the [`loadAchievements(completionHandler:)`](./gkachievement/loadachievements%28completionhandler%29.md) method to load all the achievements that the local player is progressing toward. If an achievement doesn’t load, then it’s the first time you’re reporting the player’s progress toward it, and you must create a [`GKAchievement`](./gkachievement.md) object to represent it. Next, set the percentage complete of the achievement using the [`percentComplete`](./gkachievement/percentcomplete.md) property.

You can report the player’s progress for one or more achievements to Game Center using the [`report(_:withCompletionHandler:)`](./gkachievement/report%28_,withcompletionhandler%29.md) method. The dashboard changes the appearance of the achievements to show the current percentages. If you set the percentage of an achievement to 100, the dashboard shows it as completed.

To reset the player’s progress on all achievements, use the [`resetAchievements(completionHandler:)`](./gkachievement/resetachievements%28completionhandler%29.md) class method.

## Topics

### Loading and Initializing Achievements
- [class func loadAchievements(completionHandler: (([GKAchievement]?, (any Error)?) -> Void)?)](./gkachievement/loadachievements%28completionhandler%29.md)
  Loads the achievements that you previously reported the player making progress toward.
- [init(identifier: String)](./gkachievement/init%28identifier%29.md)
  Initializes an achievement for the local player.
- [init(identifier: String, player: GKPlayer)](./gkachievement/init%28identifier,player%29.md)
  Initializes an achievement for a player.
### Accessing Achievement Properties
- [var identifier: String](./gkachievement/identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var player: GKPlayer](./gkachievement/player.md)
  The player who earned the achievement.
- [var percentComplete: Double](./gkachievement/percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var isCompleted: Bool](./gkachievement/iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
- [var lastReportedDate: Date](./gkachievement/lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.
### Reporting Progress on Achievements
- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](./gkachievement/report%28_,withcompletionhandler%29.md)
  Reports the player’s progress of players toward one or more achievements.
- [class func report([GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./gkachievement/report%28_,witheligiblechallenges,withcompletionhandler%29.md)
  Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.
- [var showsCompletionBanner: Bool](./gkachievement/showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](./gkachievement/resetachievements%28completionhandler%29.md)
  Resets the percentage completed for all of the player’s achievements.
### Issuing Achievement Challenges
- [func selectChallengeablePlayers([GKPlayer], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./gkachievement/selectchallengeableplayers%28_,withcompletionhandler%29.md)
  Finds the subset of players who can earn an achievement.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completion: GKChallengeComposeHandler?) -> UIViewController](./gkachievement/challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [typealias GKChallengeComposeHandler](./gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](./gkachievement/challengecomposecontroller%28withmessage,players,completionhandler%29.md)
  Provides a view controller that you present to the player to issue an achievement challenge.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](./gkachievement/challengecomposecontroller%28withplayers,message,completionhandler%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a message.
### Deprecated
- [Deprecated Symbols](./gkachievement-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Initializers
- [init?(coder: NSCoder)](./gkachievement/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Achievements
- [Rewarding players with achievements](./rewarding-players-with-achievements.md)
  Use achievements to motivate players and engage them more in your game.
- [class GKAchievementDescription](./gkachievementdescription.md)
  An object containing the text and artwork used to present an achievement to a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement)*