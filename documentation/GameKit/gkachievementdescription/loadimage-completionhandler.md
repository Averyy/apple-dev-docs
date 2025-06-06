# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the image to display when the player completes the achievement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func loadImage() async throws -> NSImage
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

#### Discussion

First, use the [`loadAchievementDescriptions(completionHandler:)`](gkachievementdescription/loadachievementdescriptions(completionhandler:).md) method to download the achievement description objects, and then use this method to download the individual achievement images. While GameKit downloads an achievement image, you can display the placeholder image. If successful, GameKit sets the image property to the image it passes to the completion handler.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func incompleteAchievementImage() -> UIImage](gkachievementdescription/incompleteachievementimage.md)
  A common image that you can display when the player hasn’t completed the achievement.
- [class func placeholderCompletedAchievementImage() -> UIImage](gkachievementdescription/placeholdercompletedachievementimage.md)
  A placeholder image that you can display when the player completes the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/loadimage(completionhandler:))*