# MTLPixelFormat.bgr10_xr

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A 32-bit extended-range pixel format with three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case bgr10_xr
```

```c
MTLPixelFormatBGR10_XR
```

## Discussion

Pixel components are in blue, green, and red order, from least significant bit to most significant bit. Bits 30 and 31 are padding, and their value is `0`.

![Bit layout diagram showing the pixel data storage arrangement of the bgr10_xr pixel format. The blue component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the red component is stored in bits 20 to 29, and bits 30 to 31 are used as padding.](https://developer.apple.com/tutorials/images/com.apple.metal/bgr10-xr-layout-1@2x.png)

Components are linearly encoded in a transform from `[0,2^10)` to [`-0.752941, 1.25098]`. The formula used in this linear encoding is `shader_float = (xr10_value - 384) / 510.0f`.

> 💡 **Tip**:  Each UNorm8-based pixel value has an exact corresponding value in the XR10 pixel range, given by `xr10_value = unorm8_value * 2 + 384`.

To display wide color values on devices with wide color displays, set this pixel format on the [`colorPixelFormat`](../../MetalKit/mtkview/colorpixelformat.md) property of an [`MTKView`](../../MetalKit/mtkview.md) or the [`pixelFormat`](../../QuartzCore/cametallayer/pixelformat.md) property of a [`CAMetalLayer`](../../QuartzCore/cametallayer.md).

> **Note**:  Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

## See Also

### Extended range and wide color pixel formats
- [MTLPixelFormat.bgra10_xr](./bgra10_xr.md)
  A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgra10_xr_srgb](./bgra10_xr_srgb.md)
  A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgr10_xr_srgb](./bgr10_xr_srgb.md)
  A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr)*