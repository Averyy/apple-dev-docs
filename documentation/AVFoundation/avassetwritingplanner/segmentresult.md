# AVAssetWritingPlanner.SegmentResult

**Framework**: AVFoundation  
**Kind**: enum

Result type for manual segment completion control.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SegmentResult
```

#### Overview

Return this type from the segment handler to explicitly control how each segment completes, including saving custom client state for resumable exports or canceling segments.

## Topics

### Completion Options
- [AVAssetWritingPlanner.SegmentResult.success](avassetwritingplanner/segmentresult/success.md)
  Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](avassetwritingplanner/segmentresult/successwithstate(_:).md)
  Finish the segment successfully with custom client state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](avassetwritingplanner/segmentresult/cancelled.md)
  Cancel the current segment while allowing future resumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult)*