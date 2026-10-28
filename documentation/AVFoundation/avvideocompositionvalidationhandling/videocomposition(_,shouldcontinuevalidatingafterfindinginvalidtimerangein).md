# videoComposition(_:shouldContinueValidatingAfterFindingInvalidTimeRangeIn:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) videoComposition:(AVVideoComposition *) videoComposition shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:(id<AVVideoCompositionInstruction>) videoCompositionInstruction;
```

## Return Value

[`true`](../../Swift/true.md) if the video composition should continue validation in order to report additional problems that may exist, otherwise [`false`](../../Swift/false.md).

## Discussion

A time range is considered invalid when it overlaps with the time range of a prior instruction, or that contains times earlier than the time range of a prior instruction

## Parameters

- `videoComposition`: The video composition being validated.
- `videoCompositionInstruction`: The video composition instruction.

## See Also

### Configuring validation methods
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidvalueforkey%29.md)
  Reports that a key that has an invalid value.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindingemptytimerange%29.md)
  Reports a time range that has no corresponding video composition instruction.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidtrackidin,layerinstruction,asset%29.md)
  Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtimerangein:))*