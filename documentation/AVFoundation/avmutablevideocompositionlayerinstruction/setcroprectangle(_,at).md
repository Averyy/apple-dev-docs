# setCropRectangle(_:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the crop rectangle  value at a time within the time range of the instruction.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
func setCropRectangle(_ cropRectangle: CGRect, at time: CMTime)
```

```objc
- (void) setCropRectangle:(CGRect) cropRectangle atTime:(CMTime) time;
```

#### Discussion

The origin of the crop rectangle is the top-left corner of the buffer clean aperture rectangle. The crop rectangle is defined in square pixel space, that is, without taking the pixel aspect ratio into account. Crop rectangles extending outside of the clean aperture, are cropped to the clean aperture.

Sets a fixed crop rectangle to apply from `time` until the next time at which a crop rectangle is set; this is the same as setting a flat ramp for that time range.

Before the first specified time for which a crop rectangle is set, the crop rectangle is held constant to [`CGRectInfinite`](../../CoreGraphics/cgrectinfinite.md) and after the last time for which a crop rectangle is set, the crop rectangle is held constant at that last value.

## Parameters

- `cropRectangle`: The crop rectangle to be applied at the specified time.
- `time`: A time value within the timeRange of the composition instruction.

## See Also

### Setting crop rectangle values
- [func setCropRectangleRamp(fromStartCropRectangle: CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)](./setcroprectangleramp%28fromstartcroprectangle,toendcroprectangle,timerange%29.md)
  Sets a crop rectangle ramp to apply during the specified time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangle(_:at:))*