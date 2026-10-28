# getCropRectangleRamp(for:startCropRectangle:endCropRectangle:timeRange:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains the crop rectangle ramp that includes the specified time.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func getCropRectangleRamp(for time: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

```objc
- (BOOL) getCropRectangleRampForTime:(CMTime) time startCropRectangle:(CGRect *) startCropRectangle endCropRectangle:(CGRect *) endCropRectangle timeRange:(CMTimeRange *) timeRange;
```

## Return Value

[`false`](../../Swift/false.md) will be returned if the specified time is beyond the duration of the last crop rectangle ramp that has been set.

## Parameters

- `time`: If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.
- `startCropRectangle`: A pointer to a `CGRect` to receive the starting crop rectangle value for the crop rectangle ramp.

  May be NULL.
- `endCropRectangle`: A pointer to a `CGRect` to receive the ending crop rectangle value for the crop rectangle ramp.

  This value may be `NULL`.
- `timeRange`: A pointer to a `CMTimeRange` to receive the time range of the crop rectangle ramp.

  This value may be `NULL`.

## See Also

### Getting opacity, transform, and cropping ramps
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](./croprectangleramp%28at%29.md)
  Obtains the crop rectangle ramp that includes the specified time.
- [AVVideoCompositionLayerInstruction.CropRectangleRamp](./croprectangleramp.md)
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](./opacityramp%28at%29.md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](./opacityramp.md)
- [func getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](./getopacityramp%28for,startopacity,endopacity,timerange%29.md)
  Obtains the opacity ramp that includes a specified time.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](./transformramp%28at%29.md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](./transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](./gettransformramp%28for,start,end,timerange%29.md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:))*