# beginTrimming(completionHandler:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Presents the system trimming interface controls inside the player view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func beginTrimming(completionHandler handler: ((Bool) -> Void)? = nil)
```

```swift
func beginTrimming() async -> Bool
```

```objc
- (void) beginTrimmingWithCompletionHandler:(void (^)(BOOL success)) handler;
```

## Mentions

- [Trimming and exporting media in visionOS](../trimming-and-exporting-media-in-visionos.md)

## Discussion

After trimming is complete, you can access the trimmed range by querying the [`forwardPlaybackEndTime`](../../AVFoundation/avplayeritem/forwardplaybackendtime.md) and [`reversePlaybackEndTime`](../../AVFoundation/avplayeritem/reverseplaybackendtime.md) properties on the [`AVPlayerItem`](../../AVFoundation/avplayeritem.md).

For more information on supporting trimming in your app, see [Trimming and exporting media in visionOS](../trimming-and-exporting-media-in-visionos.md).

## Parameters

- `handler`: A completion handler that the system calls with a Boolean value that indicates whether the user completed the trim operation, or if they canceled it.

## See Also

### Presenting the visionOS trimming UI
- [var canBeginTrimming: Bool](./canbegintrimming.md)
  A Boolean value that indicates whether the current media supports trimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/begintrimming(completionhandler:))*