# AVVideoCompositionLayerInstruction.CropRectangleRamp

**Framework**: AVFoundation  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CropRectangleRamp
```

## Topics

### Creating a crop rectangle ramp
- [init(timeRange: CMTimeRange, start: CGRect, end: CGRect)](avvideocompositionlayerinstruction/croprectangleramp/init(timerange:start:end:).md)
### Inspecting the crop rectangle ramp
- [var end: CGRect](avvideocompositionlayerinstruction/croprectangleramp/end.md)
- [var start: CGRect](avvideocompositionlayerinstruction/croprectangleramp/start.md)
- [var timeRange: CMTimeRange](avvideocompositionlayerinstruction/croprectangleramp/timerange.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](avvideocompositionlayerinstruction/opacityramp.md)
- [func getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getopacityramp(for:startopacity:endopacity:timerange:).md)
  Obtains the opacity ramp that includes a specified time.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](avvideocompositionlayerinstruction/transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:).md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/croprectangleramp)*