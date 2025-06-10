# GKAchievementDescription

**Framework**: GameKit  
**Kind**: class

An object containing the text and artwork used to present an achievement to a player.

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
class GKAchievementDescription
```

#### Overview

To present an achievement to the player in your interface, you can download the localized text and artwork for the achievements that you enter in App Store Connect. To get the localized text, use the [`loadAchievementDescriptions(completionHandler:)`](gkachievementdescription/loadachievementdescriptions(completionhandler:).md) class method. GameKit passes an array of [`GKAchievementDescription`](gkachievementdescription.md) objects to the completion handler that contains the text. To get the artwork for an achievement, use the [`loadImage(completionHandler:)`](gkachievementdescription/loadimage(completionhandler:).md) method.

To get standard images your game can use to present achievement progress to the player, use the [`incompleteAchievementImage()`](gkachievementdescription/incompleteachievementimage().md) and [`placeholderCompletedAchievementImage()`](gkachievementdescription/placeholdercompletedachievementimage().md)) class methods.

Alternatively, either add the access point or display the dashboard so that the player can view achievements and navigate to their other Game Center data.

## Topics

### Retrieving Achievement Descriptions
- [class func loadAchievementDescriptions(completionHandler: (([GKAchievementDescription]?, (any Error)?) -> Void)?)](gkachievementdescription/loadachievementdescriptions(completionhandler:).md)
  Downloads the localized descriptions of achievements from Game Center.
### Reading and Writing Achievement Properties
- [var identifier: String](gkachievementdescription/identifier.md)
  The string you enter in App Store Connect that uniquely identifies the achievement.
- [var title: String](gkachievementdescription/title.md)
  A localized title for the achievement.
- [var unachievedDescription: String](gkachievementdescription/unachieveddescription.md)
  A localized description of the achievement that you display when the player hasn’t completed the achievement.
- [var achievedDescription: String](gkachievementdescription/achieveddescription.md)
  A localized description of the achievement that you display when the player completes the achievement.
- [var maximumPoints: Int](gkachievementdescription/maximumpoints.md)
  The number of points that the player earns when completing the achievement.
- [var image: NSImage?](gkachievementdescription/image.md)
  The achievement’s artwork that you display when the player completes the achievement.
- [var isHidden: Bool](gkachievementdescription/ishidden.md)
  A Boolean value that states whether the achievement is initially visible to players.
- [var isReplayable: Bool](gkachievementdescription/isreplayable.md)
  A Boolean value that states whether the player can earn the achievement multiple times.
- [var rarityPercent: Double?](gkachievementdescription/raritypercent-4bh6k.md)
  The percentage of players of this game that earned the achievement.
### Working with Achievement Images
- [class func incompleteAchievementImage() -> UIImage](gkachievementdescription/incompleteachievementimage.md)
  A common image that you can display when the player hasn’t completed the achievement.
- [class func placeholderCompletedAchievementImage() -> UIImage](gkachievementdescription/placeholdercompletedachievementimage.md)
  A placeholder image that you can display when the player completes the achievement.
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkachievementdescription/loadimage(completionhandler:).md)
  Loads the image to display when the player completes the achievement.
### Retrieving Group Information
- [var groupIdentifier: String?](gkachievementdescription/groupidentifier.md)
  The identifier for the group that the achievement description is part of.
### Instance Properties
- [var activityIdentifier: String](gkachievementdescription/activityidentifier.md)
  The identifier of the game activity associated with this achievement, as configured by the developer in App Store Connect.
- [var activityProperties: [String : String]](gkachievementdescription/activityproperties.md)
  The properties when associating this achievement with a game activity, as configured by the developer in App Store Connect.
- [var releaseState: GKReleaseState](gkachievementdescription/releasestate.md)
  The release state of the achievement in App Store Connect.

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

- [Rewarding players with achievements](rewarding-players-with-achievements.md)
  Use achievements to motivate players and engage them more in your game.
- [class GKAchievement](gkachievement.md)
  An achievement you can award a player as they make progress toward and reach a goal in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription)*