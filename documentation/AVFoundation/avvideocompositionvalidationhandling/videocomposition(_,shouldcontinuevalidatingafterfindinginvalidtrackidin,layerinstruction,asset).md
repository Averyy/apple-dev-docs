# videoComposition(_:shouldContinueValidatingAfterFindingInvalidTrackIDIn:layerInstruction:asset:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn videoCompositionInstruction: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool
```

```objc
- (BOOL) videoComposition:(AVVideoComposition *) videoComposition shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:(id<AVVideoCompositionInstruction>) videoCompositionInstruction layerInstruction:(AVVideoCompositionLayerInstruction *) layerInstruction asset:(AVAsset *) asset;
```

## Return Value

[`true`](../../Swift/true.md) if the video composition should continue validation in order to report additional problems that may exist, otherwise [`false`](../../Swift/false.md).

## Discussion

The asset track is specified in the [`isValid(for:timeRange:validationDelegate:)`](../avvideocomposition/isvalid%28for,timerange,validationdelegate%29.md) method.

## Parameters

- `videoComposition`: The video composition being validated.
- `videoCompositionInstruction`: The video composition instruction.
- `layerInstruction`: The layer instruction.
- `asset`: The underlying asset.

## See Also

### Configuring validation methods
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidvalueforkey%29.md)
  Reports that a key that has an invalid value.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindingemptytimerange%29.md)
  Reports a time range that has no corresponding video composition instruction.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn: any AVVideoCompositionInstructionProtocol) -> Bool](./videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidtimerangein%29.md)
  Reports a video composition instruction with a time range that is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtrackidin:layerinstruction:asset:))*