# videoComposition(_:shouldContinueValidatingAfterFindingEmptyTimeRange:)

**Framework**: AVFoundation  
**Kind**: method

Reports a time range that has no corresponding video composition instruction.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the video composition should continue validation in order to report additional problems that may exist, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `videoComposition`: The video composition being validated.
- `timeRange`: The time range that has no corresponding video composition instruction.

## See Also

- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidvalueforkey:).md)
  Reports that a key that has an invalid value.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn: any AVVideoCompositionInstructionProtocol) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtimerangein:).md)
  Reports a video composition instruction with a time range that is invalid.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtrackidin:layerinstruction:asset:).md)
  Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindingemptytimerange:))*