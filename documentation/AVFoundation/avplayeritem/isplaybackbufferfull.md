# isPlaybackBufferFull

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
var isPlaybackBufferFull: Bool { get }
```

```objc
@property (readonly, getter=isPlaybackBufferFull) BOOL playbackBufferFull;
```

## Discussion

Despite the playback buffer reaching capacity there might not exist sufficient statistical data to support a [`isPlaybackLikelyToKeepUp`](./isplaybacklikelytokeepup.md) prediction of [`true`](../../Swift/true.md).

## See Also

### Determining buffering status
- [var isPlaybackLikelyToKeepUp: Bool](./isplaybacklikelytokeepup.md)
  A Boolean value that indicates whether the item will likely play through without stalling.
- [var isPlaybackBufferEmpty: Bool](./isplaybackbufferempty.md)
  A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybackbufferfull)*