# videoComposition(_:shouldContinueValidatingAfterFindingInvalidTimeRangeIn:)

**Framework**: AVFoundation  
**Kind**: method

Reports a video composition instruction with a time range that is invalid.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn videoCompositionInstruction: any AVVideoCompositionInstructionProtocol) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the video composition should continue validation in order to report additional problems that may exist, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

A time range is considered invalid when it overlaps with the time range of a prior instruction, or that contains times earlier than the time range of a prior instruction

## Parameters

- `videoComposition`: The video composition being validated.
- `videoCompositionInstruction`: The video composition instruction.

## See Also

- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidvalueforkey:).md)
  Reports that a key that has an invalid value.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindingemptytimerange:).md)
  Reports a time range that has no corresponding video composition instruction.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtrackidin:layerinstruction:asset:).md)
  Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtimerangein:))*