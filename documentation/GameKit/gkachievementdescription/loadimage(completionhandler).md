# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the image to display when the player completes the achievement.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadImage(completionHandler: (@Sendable (UIImage?, (any Error)?) -> Void)? = nil)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadImage() async throws -> UIImage
```

*macOS*

```swift
func loadImage(completionHandler: (@Sendable (NSImage?, (any Error)?) -> Void)? = nil)
```

*macOS*

```swift
func loadImage() async throws -> NSImage
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(UIImage *image, NSError *error)) completionHandler;
```

*macOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error)) completionHandler;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

#### Discussion

First, use the [`loadAchievementDescriptions(completionHandler:)`](./loadachievementdescriptions%28completionhandler%29.md) method to download the achievement description objects, and then use this method to download the individual achievement images. While GameKit downloads an achievement image, you can display the placeholder image. If successful, GameKit sets the image property to the image it passes to the completion handler.

## Parameters

- `completionHandler`: A block that GameKit calls when this method completes the download.

  The block receives the following parameters:

  - **`image`**: The image that represents the completed achievement. This parameter is `nil` if an error occurs.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Working with Achievement Images
- [class func incompleteAchievementImage() -> UIImage](./incompleteachievementimage%28%29.md)
  A common image that you can display when the player hasn’t completed the achievement.
- [class func placeholderCompletedAchievementImage() -> UIImage](./placeholdercompletedachievementimage%28%29.md)
  A placeholder image that you can display when the player completes the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/loadimage(completionhandler:))*