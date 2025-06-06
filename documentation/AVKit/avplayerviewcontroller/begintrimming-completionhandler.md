# beginTrimming(completionHandler:)

**Framework**: AVKit  
**Kind**: method

Presents the system trimming interface controls inside the player view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginTrimming() async -> Bool
```

## Mentions

- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)

#### Discussion

After trimming is complete, you can access the trimmed range by querying the [`forwardPlaybackEndTime`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/forwardPlaybackEndTime) and [`reversePlaybackEndTime`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/reversePlaybackEndTime) properties on the [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem).

For more information on supporting trimming in your app, see [`Trimming and exporting media in visionOS`](trimming-and-exporting-media-in-visionos.md).

## Parameters

- `handler`: A completion handler that the system calls with a Boolean value that indicates whether the user completed the trim operation, or if they canceled it.

## See Also

- [var canBeginTrimming: Bool](avplayerviewcontroller/canbegintrimming.md)
  A Boolean value that indicates whether the current media supports trimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/begintrimming(completionhandler:))*