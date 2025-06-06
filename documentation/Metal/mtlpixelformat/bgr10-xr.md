# MTLPixelFormat.bgr10_xr

**Framework**: Metal  
**Kind**: case

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

#### Discussion

Pixel components are in blue, green, and red order, from least significant bit to most significant bit. Bits 30 and 31 are padding, and their value is `0`.

![Bit layout diagram showing the pixel data storage arrangement of the bgr10_xr pixel format. The blue component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the red component is stored in bits 20 to 29, and bits 30 to 31 are used as padding.](https://docs-assets.developer.apple.com/published/8b8b5ef3d46f2f39a29d9230a1a67a11/media-2952459%402x.png)

Components are linearly encoded in a transform from `[0,2^10)` to [`-0.752941, 1.25098]`. The formula used in this linear encoding is `shader_float = (xr10_value - 384) / 510.0f`.

> 💡 **Tip**:  Each UNorm8-based pixel value has an exact corresponding value in the XR10 pixel range, given by `xr10_value = unorm8_value * 2 + 384`.

 Each UNorm8-based pixel value has an exact corresponding value in the XR10 pixel range, given by `xr10_value = unorm8_value * 2 + 384`.

To display wide color values on devices with wide color displays, set this pixel format on the [`colorPixelFormat`](https://developer.apple.com/documentation/MetalKit/MTKView/colorPixelFormat) property of an [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) or the [`pixelFormat`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/pixelFormat) property of a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer).

> **Note**:  Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

 Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

## See Also

- [MTLPixelFormat.bgra10_xr](mtlpixelformat/bgra10_xr.md)
  A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgra10_xr_srgb](mtlpixelformat/bgra10_xr_srgb.md)
  A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgr10_xr_srgb](mtlpixelformat/bgr10_xr_srgb.md)
  A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr)*