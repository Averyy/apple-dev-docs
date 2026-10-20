# AVVideoCompositionValidationHandling

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVVideoCompositionValidationHandling : NSObjectProtocol
```

```objc
@protocol AVVideoCompositionValidationHandling <NSObject>
```

#### Overview

You might chose to stop validation after particular errors have been found so as to avoid unnecessary subsequent processing following an eror from which there is no suitable recovery.

## Topics

### Configuring validation methods
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](./avvideocompositionvalidationhandling/videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidvalueforkey%29.md)
  Reports that a key that has an invalid value.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool](./avvideocompositionvalidationhandling/videocomposition%28_,shouldcontinuevalidatingafterfindingemptytimerange%29.md)
  Reports a time range that has no corresponding video composition instruction.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn: any AVVideoCompositionInstructionProtocol) -> Bool](./avvideocompositionvalidationhandling/videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidtimerangein%29.md)
  Reports a video composition instruction with a time range that is invalid.
- [func videoComposition(AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](./avvideocompositionvalidationhandling/videocomposition%28_,shouldcontinuevalidatingafterfindinginvalidtrackidin,layerinstruction,asset%29.md)
  Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Validating the time range
- [func isValid(for: [AVAssetTrack], assetDuration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./avvideocomposition/isvalid%28for,assetduration,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](./avvideocomposition/determinevalidity%28for,timerange,validationdelegate,completionhandler%29.md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.
- [func isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./avvideocomposition/isvalid%28for,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling)*