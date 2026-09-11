# AVAssetWritingPlanner.SegmentResult.cancelled

**Framework**: AVFoundation  
**Kind**: case

Cancel the current segment while allowing future resumption.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case cancelled
```

#### Discussion

Use this case when the segment should be canceled (for example, due to background task expiration) but you expect to resume the export later. This preserves the ability to restart from this segment in a future export session.

This is equivalent to calling `cancel()` on the segment request.

#### Use Cases

- Background task expiration handler called
- System resources unavailable
- User-initiated pause operation

## See Also

- [AVAssetWritingPlanner.SegmentResult.success](avassetwritingplanner/segmentresult/success.md)
  Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](avassetwritingplanner/segmentresult/successwithstate(_:).md)
  Finish the segment successfully with custom client state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/cancelled)*