# sequenceWasRestarted

**Framework**: AVFoundation  
**Kind**: property

Indicates the very first buffer in a new sequence produced by this output. Seeking or changing playback direction will start a new sequence of buffers. If you have any sample buffers queued from the previous sequence, these should be discarded.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var sequenceWasRestarted: Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence/sequencewasrestarted)*