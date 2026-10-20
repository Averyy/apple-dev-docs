# loadPhoto(for:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads a photo of the player from Game Center.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadPhoto(for size: GKPlayer.PhotoSize, withCompletionHandler completionHandler: (@Sendable (UIImage?, (any Error)?) -> Void)? = nil)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadPhoto(for size: GKPlayer.PhotoSize) async throws -> UIImage
```

*macOS*

```swift
func loadPhoto(for size: GKPlayer.PhotoSize, withCompletionHandler completionHandler: (@Sendable (NSImage?, (any Error)?) -> Void)? = nil)
```

*macOS*

```swift
func loadPhoto(for size: GKPlayer.PhotoSize) async throws -> NSImage
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) loadPhotoForSize:(GKPhotoSize) size withCompletionHandler:(void (^)(UIImage *photo, NSError *error)) completionHandler;
```

*macOS*

```objc
- (void) loadPhotoForSize:(GKPhotoSize) size withCompletionHandler:(void (^)(NSImage *photo, NSError *error)) completionHandler;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The size of the image that returns to your game is dependent on both the size parameter and the user interface idiom of the device your game is running on.

## Parameters

- `size`: A constant that determines the size of the photo to load.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***photo***: An image of the player. If an error occurs, this may be a cached image already on the device; otherwise, it is `nil`.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading player photos
- [GKPlayer.PhotoSize](./photosize.md)
  The size of a photo that Game Center loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/loadphoto(for:withcompletionhandler:))*