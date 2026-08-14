# AVAssetWritingPlanner.SegmentBoundaryGuidelines

**Framework**: AVFoundation  
**Kind**: struct

AVPlannedVideoSegmentBoundaryGuidelines provides guidance on determining planned segment boundaries for a video track in an incremental writing session executed by the AVAssetWritingPlanner.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SegmentBoundaryGuidelines
```

#### Overview

The properties provide guidance on determining segment boundaries for a video track in an incremental writing session. All conditions should be supported for best results. The client should choose frame count and minimum duration that meet the minimum requirement. However, the client should also consider the balance between overhead caused by completing and saving states for small segments, and the cost of having to redo a large segment if the incremental session stopped in the middle of a segment due to errors or crashes. For example, use 1 minute segments for 4K60fps video.

## Topics

### Initializers
- [init()](avassetwritingplanner/segmentboundaryguidelines/init.md)
- [init(minimumFrameCount: Int, minimumDuration: CMTime)](avassetwritingplanner/segmentboundaryguidelines/init(minimumframecount:minimumduration:).md)
### Instance Properties
- [var minimumDuration: CMTime](avassetwritingplanner/segmentboundaryguidelines/minimumduration.md)
  The minimum duration of each incremental segment. kCMTimeZero means there is no minimum segment duration requirement. kCMTimePositiveInfinity means that incremental segmentation is not supported for this codecType.
- [var minimumFrameCount: Int](avassetwritingplanner/segmentboundaryguidelines/minimumframecount.md)
  The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines)*