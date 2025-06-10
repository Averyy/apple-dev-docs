# placeholderCompletedAchievementImage()

**Framework**: GameKit  
**Kind**: method

A placeholder image that you can display when the player completes the achievement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func placeholderCompletedAchievementImage() -> NSImage
```

#### Return Value

A common image that represents a completed achievement.

#### Discussion

When the player completes the achievement, you can display this image as a placeholder until GameKit downloads the achievement’s image that you upload to App Store Connect.

In macOS versions earlier than macOS 11, this class method returns an [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) object but otherwise works the same as in iOS, Mac Catalyst, and tvOS.

Starting with iOS 14, macOS 11, and tvOS 14, this method returns a symbol image. To match your game’s appearance, make adjustments to the symbol image as described in [`Configuring and displaying symbol images in your UI`](https://developer.apple.com/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui).

## See Also

- [class func incompleteAchievementImage() -> UIImage](gkachievementdescription/incompleteachievementimage.md)
  A common image that you can display when the player hasn’t completed the achievement.
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkachievementdescription/loadimage(completionhandler:).md)
  Loads the image to display when the player completes the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/placeholdercompletedachievementimage())*