# transformRamp(at:)

**Framework**: AVFoundation  
**Kind**: method

Obtains the transform ramp that includes a specified time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func transformRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?
```

## See Also

- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [AVVideoCompositionLayerInstruction.CropRectangleRamp](avvideocompositionlayerinstruction/croprectangleramp.md)
- [func getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](avvideocompositionlayerinstruction/opacityramp.md)
- [func getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getopacityramp(for:startopacity:endopacity:timerange:).md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](avvideocompositionlayerinstruction/transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:).md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/transformramp(at:))*