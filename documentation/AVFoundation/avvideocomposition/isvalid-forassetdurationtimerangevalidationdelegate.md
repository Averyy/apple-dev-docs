# isValid(for:assetDuration:timeRange:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method

Indicates whether the time ranges of the composition’s instructions conform to validation requirements.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func isValid(for tracks: [AVAssetTrack], assetDuration duration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the validation succeeds; otherwise; [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `tracks`: Pass a reference to an asset’s tracks if you wish to validate the track IDs of the layer instructions against the asset’s tracks. Pass   to skip that validation. This method throws an exception if the tracks aren’t all from the same asset.
- `duration`: Pass the asset duration to validate the time ranges of the instructions. Pass   to skip that validation.
- `timeRange`: The composition only validates those instructions with time ranges that overlap with the specified time range. To validate all instructions that the composition may use for playback or other processing, regardless of time range, pass  .
- `validationDelegate`: A delegate that handles validation requests. May be  .

## See Also

- [protocol AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:).md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.
- [func isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](avvideocomposition/isvalid(for:timerange:validationdelegate:).md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:))*