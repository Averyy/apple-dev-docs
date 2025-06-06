# determineValidity(for:timeRange:validationDelegate:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether the time ranges of the composition’s instructions conform to validation requirements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func isValid(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) async throws -> Bool
```

#### Discussion

During validation, the video composition calls the validation delegate, if one exists, with a reference to any trouble spots in the video composition.

This method raises an exception if the delegate modifies the video composition’s instructions, or the array of layer instructions of any [`AVVideoCompositionInstruction`](avvideocompositioninstruction-swift.class.md) object contained therein during validation.

## Parameters

- `asset`: An asset object, if you require validating the time ranges of the instructions against the duration of the asset and the track IDs of the layer instructions against the asset’s tracks. Pass   to skip that validation.
- `timeRange`: A time range over which to validate instructions. The method validates only instructions with time ranges that overlap with this time range. To validate all instructions that you can use for playback or other processing, regardless of time range, pass  .
- `validationDelegate`: An object that adopts the   protocol to receive detailed information about problematic sections of a video composition during processing. Pass   if you don’t require the details.
- `completionHandler`: A block the system calls when it determines whether the video composition is valid.

## See Also

- [func isValid(for: [AVAssetTrack], assetDuration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:).md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [protocol AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](avvideocomposition/isvalid(for:timerange:validationdelegate:).md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:))*