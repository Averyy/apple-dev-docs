# isPlaybackBufferFull

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
var isPlaybackBufferFull: Bool { get }
```

#### Discussion

Despite the playback buffer reaching capacity there might not exist sufficient statistical data to support a [`isPlaybackLikelyToKeepUp`](avplayeritem/isplaybacklikelytokeepup.md) prediction of [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var isPlaybackLikelyToKeepUp: Bool](avplayeritem/isplaybacklikelytokeepup.md)
  A Boolean value that indicates whether the item will likely play through without stalling.
- [var isPlaybackBufferEmpty: Bool](avplayeritem/isplaybackbufferempty.md)
  A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybackbufferfull)*