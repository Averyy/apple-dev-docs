# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the localized image that you associate with the leaderboard set.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func loadImage(completionHandler: (@Sendable (UIImage?, (any Error)?) -> Void)? = nil)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(UIImage *image, NSError *error)) completionHandler;
```

*macOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block that GameKit calls when this method completes the request.

  The block receives the following parameters:

  - ***image***: The image for the leaderboard set. If an error occurs, this property may be non-`nil` and contain data GameKit loads before the error occurs.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboard Sets
- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](./loadleaderboardsets%28completionhandler%29.md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](./loadleaderboards%28handler%29.md)
  Loads the leaderboards in the leaderboard set.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadimage(completionhandler:))*