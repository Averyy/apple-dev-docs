# isPlaybackBufferEmpty

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.

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
var isPlaybackBufferEmpty: Bool { get }
```

## See Also

- [var isPlaybackLikelyToKeepUp: Bool](avplayeritem/isplaybacklikelytokeepup.md)
  A Boolean value that indicates whether the item will likely play through without stalling.
- [var isPlaybackBufferFull: Bool](avplayeritem/isplaybackbufferfull.md)
  A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isplaybackbufferempty)*