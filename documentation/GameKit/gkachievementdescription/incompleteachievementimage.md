# incompleteAchievementImage()

**Framework**: GameKit  
**Kind**: method

A common image that you can display when the player hasn’t completed the achievement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func incompleteAchievementImage() -> NSImage
```

#### Return Value

A common image that represents an incomplete achievement.

#### Discussion

In macOS versions earlier than macOS 11, this class method returns an [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) object but otherwise works the same as in iOS, Mac Catalyst, and tvOS.

Starting with iOS 14, macOS 11, and tvOS 14, this method returns a symbol image. To match your game’s appearance, make adjustments to the symbol image as described in [`Configuring and displaying symbol images in your UI`](https://developer.apple.com/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui).

## See Also

- [class func placeholderCompletedAchievementImage() -> UIImage](gkachievementdescription/placeholdercompletedachievementimage.md)
  A placeholder image that you can display when the player completes the achievement.
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkachievementdescription/loadimage(completionhandler:).md)
  Loads the image to display when the player completes the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/incompleteachievementimage())*