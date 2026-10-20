# isValid(for:assetDuration:timeRange:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isValidForTracks:(NSArray<AVAssetTrack *> *) tracks assetDuration:(CMTime) duration timeRange:(CMTimeRange) timeRange validationDelegate:(id<AVVideoCompositionValidationHandling>) validationDelegate;
```

#### Return Value

[`true`](../../Swift/true.md) if the validation succeeds; otherwise; [`false`](../../Swift/false.md).

## Parameters

- `tracks`: Pass a reference to an asset’s tracks if you wish to validate the track IDs of the layer instructions against the asset’s tracks. Pass `nil` to skip that validation. This method throws an exception if the tracks aren’t all from the same asset.
- `duration`: Pass the asset duration to validate the time ranges of the instructions. Pass [`invalid`](../../CoreMedia/cmtime/invalid.md) to skip that validation.
- `timeRange`: The composition only validates those instructions with time ranges that overlap with the specified time range. To validate all instructions that the composition may use for playback or other processing, regardless of time range, pass `CMTimeRange(start: .zero, end: .positiveInfinity)`.
- `validationDelegate`: A delegate that handles validation requests. May be `nil`.

## See Also

### Validating the time range
- [protocol AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](./determinevalidity%28for,timerange,validationdelegate,completionhandler%29.md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.
- [func isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./isvalid%28for,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:))*