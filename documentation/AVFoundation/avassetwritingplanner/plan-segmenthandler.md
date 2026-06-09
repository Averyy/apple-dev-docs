# plan(_:segmentHandler:)

**Framework**: AVFoundation  
**Kind**: method

Adds a track plan with manual segment completion control.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func plan(_ trackPlan: AVAssetTrackPlan, segmentHandler: @escaping @Sendable (AVPlannedSegmentWritingRequest) async throws -> AVAssetWritingPlanner.SegmentResult)
```

#### Discussion

This variant provides fine-grained control over segment completion, allowing you to return a [`AVAssetWritingPlanner.SegmentResult`](avassetwritingplanner/segmentresult.md) that explicitly controls how the segment completes.

## Parameters

- `trackPlan`: The track plan contains information about the track and boundaries of all the segments.
- `segmentHandler`: Handler that returns a [`AVAssetWritingPlanner.SegmentResult`](avassetwritingplanner/segmentresult.md) for manual control.

## Topics

### See Also
- [AVAssetWritingPlanner.SegmentResult](avassetwritingplanner/segmentresult.md)
  Result type for manual segment completion control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/plan(_:segmenthandler:))*