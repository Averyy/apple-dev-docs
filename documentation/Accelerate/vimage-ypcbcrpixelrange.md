# vImage_YpCbCrPixelRange

**Framework**: Accelerate  
**Kind**: struct

The description of range and clamping information for YpCbCr pixel formats.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImage_YpCbCrPixelRange
```

#### Overview

Y’CbCr formats frequently don’t use the entire representable range available to them to represent image data. While a  video format does use the entire range, a  format often leaves the extrema unused, except perhaps to represent values outside of the standard `Y'=[0,1]` `CbCr = [-0.5,0.5]` range. For example, an 8-bit video range format typically uses the range `[16,235]` for Y’ and `[16,240]` for Cb and Cr.

The following code shows examples of typical Y’CbCr pixel ranges:

```swift
// The 8-bit pixel range that's unclamped.
let pixelRange = vImage_YpCbCrPixelRange(Yp_bias: 16,
                                         CbCr_bias: 128,
                                         YpRangeMax: 235,
                                         CbCrRangeMax: 240,
                                         YpMax: 255,
                                         YpMin: 0,
                                         CbCrMax: 255,
                                         CbCrMin: 1)

 // The 8-bit pixel range that's clamped to video range.
let pixelRange = vImage_YpCbCrPixelRange(Yp_bias: 16,
                                         CbCr_bias: 128,
                                         YpRangeMax: 265,
                                         CbCrRangeMax: 240,
                                         YpMax: 235,
                                         YpMin: 16,
                                         CbCrMax: 240,
                                         CbCrMin: 16)
        
// The 8-bit pixel range that's clamped to full range.
let pixelRange = vImage_YpCbCrPixelRange(Yp_bias: 0,
                                         CbCr_bias: 128,
                                         YpRangeMax: 255,
                                         CbCrRangeMax: 255,
                                         YpMax: 255,
                                         YpMin: 1,
                                         CbCrMax: 255,
                                         CbCrMin: 0)
```

The bias is the prebias for YUV to RGB and the postbias for RGB to YUV.

## Topics

### Creating a Pixel Range
- [init(Yp_bias: Int32, CbCr_bias: Int32, YpRangeMax: Int32, CbCrRangeMax: Int32, YpMax: Int32, YpMin: Int32, CbCrMax: Int32, CbCrMin: Int32)](vimage_ypcbcrpixelrange/init(yp_bias:cbcr_bias:yprangemax:cbcrrangemax:ypmax:ypmin:cbcrmax:cbcrmin:).md)
  Returns a structure describing range and clamping information for Y’CbCr pixel formats.
- [init()](vimage_ypcbcrpixelrange/init.md)
### Pixel Range Properties
- [var Yp_bias: Int32](vimage_ypcbcrpixelrange/yp_bias.md)
  The encoding for `Y' = 0.0` for this video format (varies by bit depth).
- [var CbCr_bias: Int32](vimage_ypcbcrpixelrange/cbcr_bias.md)
  The encoding for `{Cb, Cr} = 0.0` for this video format.
- [var YpRangeMax: Int32](vimage_ypcbcrpixelrange/yprangemax.md)
  The encoding for `Y' = 1.0` for this video format.
- [var CbCrRangeMax: Int32](vimage_ypcbcrpixelrange/cbcrrangemax.md)
  The encoding for `{Cb, Cr} = 0.5` for this video format.
- [var YpMax: Int32](vimage_ypcbcrpixelrange/ypmax.md)
  The encoding for the maximum allowed Y’ value.
- [var YpMin: Int32](vimage_ypcbcrpixelrange/ypmin.md)
  The encoding of the minimum allowed Y’ value.
- [var CbCrMax: Int32](vimage_ypcbcrpixelrange/cbcrmax.md)
  The encoding of the maximum allowed `{Cb, Cr}` value.
- [var CbCrMin: Int32](vimage_ypcbcrpixelrange/cbcrmin.md)
  The encoding of the minimum allowed `{Cb, Cr}` value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageConvert_ARGBToYpCbCr_GenerateConversion(UnsafePointer<vImage_ARGBToYpCbCrMatrix>, UnsafePointer<vImage_YpCbCrPixelRange>, UnsafeMutablePointer<vImage_ARGBToYpCbCr>, vImageARGBType, vImageYpCbCrType, vImage_Flags) -> vImage_Error](vimageconvert_argbtoypcbcr_generateconversion(_:_:_:_:_:_:).md)
  Generates the information that describes the conversion from ARGB to YpCbCr.
- [struct vImageYpCbCrType](vimageypcbcrtype.md)
  Constants that describe the encoding of a YpCbCr image for conversions between RGB and YpCbCr.
- [struct vImageARGBType](vimageargbtype.md)
  Constants that describe the encoding of an ARGB image for conversions between RGB and YpCbCr.
- [struct vImage_ARGBToYpCbCrMatrix](vimage_argbtoypcbcrmatrix.md)
  The 3 x 3 matrix that the vImage library uses to convert from RGB to YpCbCr.
- [struct vImage_ARGBToYpCbCr](vimage_argbtoypcbcr.md)
  The information that describes the conversion from ARGB to YpCbCr.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrpixelrange)*