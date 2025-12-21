# isValid(for:timeRange:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method

Indicates whether the time ranges of the composition’s instructions conform to validation requirements.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func isValid(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the time ranges of the composition’s instructions conform to validation requirements, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Use [`determineValidity(for:timeRange:validationDelegate:completionHandler:)`](avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:).md) instead.

During validation, the video composition calls the validation delegate, if one exists, with a reference to any trouble spots in the video composition.

This method raises an exception if the delegate modifies the video composition’s instructions, or the array of layer instructions of any [`AVVideoCompositionInstruction`](avvideocompositioninstruction-swift.class.md) object contained therein during validation.

## Parameters

- `asset`: Pass   to skip that validation.
- `timeRange`: A time range over which to validate instructions. The method validates only instructions with time ranges that overlap with this time range. To validate all instructions that you can use for playback or other processing, regardless of time range, pass  .
- `validationDelegate`: Pass   if you don’t require the details.

## See Also

- [func isValid(for: [AVAssetTrack], assetDuration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:).md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [protocol AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:).md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:timerange:validationdelegate:))*