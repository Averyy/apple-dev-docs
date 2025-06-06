# MTLPixelFormat.bgr10_xr_srgb

**Framework**: Metal  
**Kind**: case

A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case bgr10_xr_srgb
```

#### Discussion

Pixel components are stored in blue, green, and red order, from least significant bit to most significant bit. Bits 30 and 31 are padding, and their value is `0`.

![Bit layout diagram showing the pixel data storage arrangement of the bgr10_xr_srgb pixel format. The blue component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the red component is stored in bits 20 to 29, and bits 30 to 31 are used as padding.](https://docs-assets.developer.apple.com/published/8b8b5ef3d46f2f39a29d9230a1a67a11/media-2952460%402x.png)

The blue, green, and red components are gamma encoded, and their values range from `-0.5271` to `1.66894`, before gamma expansion.

In order to determine a component’s value as a shader float:

- When reading a pixel, first apply the linear encoding `(xr10_value - 384) / 510.0f` and then the sRGB transform.
- When writing a pixel, first apply the sRGB transform and then the linear encoding `shader_float = (xr10_value - 384) / 510.0f`.

To display wide color values on devices with wide color displays, you set this pixel format on the [`colorPixelFormat`](https://developer.apple.com/documentation/MetalKit/MTKView/colorPixelFormat) property of an [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) or the [`pixelFormat`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/pixelFormat) property of a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer). Also provide an extended sRGB color space.

> **Note**:  Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

 Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

## See Also

- [MTLPixelFormat.bgra10_xr](mtlpixelformat/bgra10_xr.md)
  A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgra10_xr_srgb](mtlpixelformat/bgra10_xr_srgb.md)
  A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgr10_xr](mtlpixelformat/bgr10_xr.md)
  A 32-bit extended-range pixel format with three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr_srgb)*