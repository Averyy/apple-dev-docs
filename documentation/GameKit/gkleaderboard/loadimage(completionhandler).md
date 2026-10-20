# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the image for the leaderboard.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
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

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: A block that GameKit calls when this method completes the request.

  The block receives the following parameters:

  - ***image***: Contains the image for the leaderboard.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadimage(completionhandler:))*