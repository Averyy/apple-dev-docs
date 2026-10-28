# isValid(for:timeRange:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the time ranges of the composition’s instructions conform to validation requirements.

**Availability**:
- iOS 5.0+ - Deprecated in 18.0
- iPadOS 5.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Use [`isValid(for:assetDuration:timeRange:validationDelegate:)`](./isvalid%28for,assetduration,timerange,validationdelegate%29.md) instead.

## Declaration

```swift
func isValid(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool
```

```objc
- (BOOL) isValidForAsset:(AVAsset *) asset timeRange:(CMTimeRange) timeRange validationDelegate:(id<AVVideoCompositionValidationHandling>) validationDelegate;
```

## Return Value

[`true`](../../Swift/true.md) if the time ranges of the composition’s instructions conform to validation requirements, otherwise [`false`](../../Swift/false.md).

## Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Use [`determineValidity(for:timeRange:validationDelegate:completionHandler:)`](./determinevalidity%28for,timerange,validationdelegate,completionhandler%29.md) instead.

During validation, the video composition calls the validation delegate, if one exists, with a reference to any trouble spots in the video composition.

This method raises an exception if the delegate modifies the video composition’s instructions, or the array of layer instructions of any [`AVVideoCompositionInstruction`](../avvideocompositioninstruction-swift.class.md) object contained therein during validation.

## Parameters

- `asset`: An asset object, if you require validating the time ranges of the instructions against the duration of the asset and the track IDs of the layer instructions against the asset’s tracks.

  Pass `nil` to skip that validation.
- `timeRange`: A time range over which to validate instructions. The method validates only instructions with time ranges that overlap with this time range. To validate all instructions that you can use for playback or other processing, regardless of time range, pass `CMTimeRange(start: .zero, duration: .positiveInfinity)`.
- `validationDelegate`: An object that adopts the [`AVVideoCompositionValidationHandling`](../avvideocompositionvalidationhandling.md) protocol to receive detailed information about problematic sections of a video composition during processing.

  Pass `nil` if you don’t require the details.

## See Also

### Validating the time range
- [func isValid(for: [AVAssetTrack], assetDuration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./isvalid%28for,assetduration,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [protocol AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](./determinevalidity%28for,timerange,validationdelegate,completionhandler%29.md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:timerange:validationdelegate:))*