# getOpacityRamp(for:startOpacity:endOpacity:timeRange:)

**Framework**: AVFoundation  
**Kind**: method

Obtains the opacity ramp that includes a specified time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func getOpacityRamp(for time: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if values are returned successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). [`false`](https://developer.apple.com/documentation/Swift/false) is returned if `time` is beyond the duration of the last opacity ramp that has been set.

## Parameters

- `time`: If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.
- `startOpacity`: This value may be  .
- `endOpacity`: This value may be  .
- `timeRange`: This value may be  .

## See Also

- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [AVVideoCompositionLayerInstruction.CropRectangleRamp](avvideocompositionlayerinstruction/croprectangleramp.md)
- [func getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](avvideocompositionlayerinstruction/opacityramp.md)
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](avvideocompositionlayerinstruction/transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:).md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/getopacityramp(for:startopacity:endopacity:timerange:))*