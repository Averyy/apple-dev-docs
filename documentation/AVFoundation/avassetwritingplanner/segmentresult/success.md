# AVAssetWritingPlanner.SegmentResult.success

**Framework**: AVFoundation  
**Kind**: case

Finish the segment successfully without saving state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case success
```

#### Discussion

Use this case when the segment completed successfully and you don’t need to save any custom state for resumption.

This is equivalent to calling `finish()` on the segment request.

## See Also

- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](avassetwritingplanner/segmentresult/successwithstate(_:).md)
  Finish the segment successfully with custom client state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](avassetwritingplanner/segmentresult/cancelled.md)
  Cancel the current segment while allowing future resumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/success)*