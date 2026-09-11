# minimumFrameCount

**Framework**: AVFoundation  
**Kind**: property

The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var minimumFrameCount: Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumframecount)*