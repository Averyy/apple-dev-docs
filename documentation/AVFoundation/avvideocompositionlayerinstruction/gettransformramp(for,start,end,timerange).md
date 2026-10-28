# getTransformRamp(for:start:end:timeRange:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains the transform ramp that includes a specified time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func getTransformRamp(for time: CMTime, start startTransform: UnsafeMutablePointer<CGAffineTransform>?, end endTransform: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

```objc
- (BOOL) getTransformRampForTime:(CMTime) time startTransform:(CGAffineTransform *) startTransform endTransform:(CGAffineTransform *) endTransform timeRange:(CMTimeRange *) timeRange;
```

## Return Value

[`true`](../../Swift/true.md) if values are returned successfully, otherwise [`false`](../../Swift/false.md). [`false`](../../Swift/false.md) is returned if `time` is beyond the duration of the last transform ramp that has been set.

## Parameters

- `time`: If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.
- `startTransform`: A pointer to a float to receive the starting transform value for the transform ramp.

  This value may be `NULL`.
- `endTransform`: A pointer to a float to receive the ending transform value for the transform ramp.

  This value may be `NULL`.
- `timeRange`: A pointer to a `CMTimeRange` to receive the time range of the transform ramp.

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
- [func getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](./getopacityramp%28for,startopacity,endopacity,timerange%29.md)
  Obtains the opacity ramp that includes a specified time.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](./transformramp%28at%29.md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](./transformramp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:))*