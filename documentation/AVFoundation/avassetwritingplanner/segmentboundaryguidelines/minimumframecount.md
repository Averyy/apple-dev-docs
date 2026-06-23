# minimumFrameCount

**Framework**: AVFoundation  
**Kind**: property

The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var minimumFrameCount: Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumframecount)*