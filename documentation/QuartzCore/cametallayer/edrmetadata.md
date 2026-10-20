# edrMetadata

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var edrMetadata: CAEDRMetadata? { get set }
```

```objc
@property (strong, nullable) CAEDRMetadata * EDRMetadata;
```

#### Discussion

You must set this property before calling [`nextDrawable()`](./nextdrawable%28%29.md).

The default value is `nil`, which means that the system doesn’t perform any tone mapping of data prior to passing it on to the display. Values above the maximum ([`maximumExtendedDynamicRangeColorComponentValue`](../../AppKit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)) may be clipped.

If non-`nil`, the system uses the metadata provided to tone map values to the display, based on the display’s current characteristics. You must also set [`pixelFormat`](./pixelformat.md) to a pixel format that supports pixel values greater than `1.0` (such as [`MTLPixelFormat.rgba16Float`](../../Metal/mtlpixelformat/rgba16float.md)) and [`colorspace`](../caopengllayer/colorspace.md) to a color space that supports a linear transfer function.

The tone mapping process requires significant amounts of memory and GPU processing.

## See Also

### Configuring Extended Dynamic Range Behavior
- [var wantsExtendedDynamicRangeContent: Bool](./wantsextendeddynamicrangecontent.md)
  Enables extended dynamic range values onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/edrmetadata)*