# AVAssetWritingPlanner.SegmentBoundaryGuidelines

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

AVPlannedVideoSegmentBoundaryGuidelines provides guidance on determining planned segment boundaries for a video track in an incremental writing session executed by the AVAssetWritingPlanner.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SegmentBoundaryGuidelines
```

```c
typedef struct { ... } AVPlannedVideoSegmentBoundaryGuidelines;
```

## Overview

The properties provide guidance on determining segment boundaries for a video track in an incremental writing session. All conditions should be supported for best results. The client should choose frame count and minimum duration that meet the minimum requirement. However, the client should also consider the balance between overhead caused by completing and saving states for small segments, and the cost of having to redo a large segment if the incremental session stopped in the middle of a segment due to errors or crashes. For example, use 1 minute segments for 4K60fps video.

## Topics

### Initializers
- [init()](./segmentboundaryguidelines/init%28%29.md)
- [init(minimumFrameCount: Int, minimumDuration: CMTime)](./segmentboundaryguidelines/init%28minimumframecount,minimumduration%29.md)
### Instance Properties
- [var minimumDuration: CMTime](./segmentboundaryguidelines/minimumduration.md)
  The minimum duration of each incremental segment. kCMTimeZero means there is no minimum segment duration requirement. kCMTimePositiveInfinity means that incremental segmentation is not supported for this codecType.
- [var minimumFrameCount: Int](./segmentboundaryguidelines/minimumframecount.md)
  The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Sendable](../../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines)*