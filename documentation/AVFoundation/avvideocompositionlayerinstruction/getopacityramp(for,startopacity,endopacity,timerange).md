# getOpacityRamp(for:startOpacity:endOpacity:timeRange:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) getOpacityRampForTime:(CMTime) time startOpacity:(float *) startOpacity endOpacity:(float *) endOpacity timeRange:(CMTimeRange *) timeRange;
```

## Return Value

[`true`](../../Swift/true.md) if values are returned successfully, otherwise [`false`](../../Swift/false.md). [`false`](../../Swift/false.md) is returned if `time` is beyond the duration of the last opacity ramp that has been set.

## Parameters

- `time`: If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.
- `startOpacity`: A pointer to a float to receive the starting opacity value for the opacity ramp.

  This value may be `NULL`.
- `endOpacity`: A pointer to a float to receive the ending opacity value for the opacity ramp.

  This value may be `NULL`.
- `timeRange`: A pointer to a `CMTimeRange` to receive the time range of the opacity ramp.

  This value may be `NULL`.

## See Also

### Getting opacity, transform, and cropping ramps
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](./croprectangleramp%28at%29.md)
  Obtains the crop rectangle ramp that includes the specified time.
- [AVVideoCompositionLayerInstruction.CropRectangleRamp](./croprectangleramp.md)
- [func getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](./getcroprectangleramp%28for,startcroprectangle,endcroprectangle,timerange%29.md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](./opacityramp%28at%29.md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](./opacityramp.md)
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](./transformramp%28at%29.md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](./transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](./gettransformramp%28for,start,end,timerange%29.md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/getopacityramp(for:startopacity:endopacity:timerange:))*