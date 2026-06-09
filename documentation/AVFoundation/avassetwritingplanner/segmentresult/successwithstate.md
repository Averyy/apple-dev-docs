# AVAssetWritingPlanner.SegmentResult.successWithState(_:)

**Framework**: AVFoundation  
**Kind**: case

Finish the segment successfully with custom client state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case successWithState(Data)
```

#### Discussion

Use this case to save custom state data that will be restored if the export session is interrupted and later resumed. The client state is available via [`clientStateToRestore`](avplannedsegmentwritingrequest/clientstatetorestore.md) when the segment is resumed. Only the last successful state data is persisted. Any previous state data will be overwritten.

## Parameters

- `clientState`: Custom data to save for this segment. Commonly used to save algorithm state, progress information, or metadata needed for resumption.

## See Also

- [AVAssetWritingPlanner.SegmentResult.success](avassetwritingplanner/segmentresult/success.md)
  Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](avassetwritingplanner/segmentresult/cancelled.md)
  Cancel the current segment while allowing future resumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/successwithstate(_:))*