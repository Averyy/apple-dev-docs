# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the image for the leaderboard.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func loadImage() async throws -> NSImage
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: A block that GameKit calls when this method completes the request. The block receives the following parameters: - ***image***: Contains the image for the leaderboard.
- ***error***: Describes an error if it occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadimage(completionhandler:))*