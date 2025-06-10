# vImageYpCbCrType

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the encoding of a YpCbCr image for conversions between RGB and YpCbCr.

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
struct vImageYpCbCrType
```

## Topics

### Constants
- [init(UInt32)](vimageypcbcrtype/init(_:).md)
  Creates a new YpCbCr type.
- [init(rawValue: UInt32)](vimageypcbcrtype/init(rawvalue:).md)
  Creates a new YpCbCr type with an unsigned integer value.
- [var rawValue: UInt32](vimageypcbcrtype/rawvalue.md)
  The unsigned integer raw value.
- [var kvImage420Yp8_Cb8_Cr8: vImageYpCbCrType](kvimage420yp8_cb8_cr8.md)
  Any y420 or f420 (planar component Y’CbCr 8-bit 4:2:0) buffer.
- [var kvImage420Yp8_CbCr8: vImageYpCbCrType](kvimage420yp8_cbcr8.md)
  Any 420v or 420f (biplanar component Y’CbCr 8-bit 4:2:0, video-range) buffer.
- [var kvImage422CbYpCrYp16: vImageYpCbCrType](kvimage422cbypcryp16.md)
  Any v216 (component Y’CbCr 10,12,14,16-bit 4:2:2) buffer.
- [var kvImage422CbYpCrYp8: vImageYpCbCrType](kvimage422cbypcryp8.md)
  Any 2vuy (component Y’CbCr 8-bit 4:2:2) buffer.
- [var kvImage422CbYpCrYp8_AA8: vImageYpCbCrType](kvimage422cbypcryp8_aa8.md)
  Any a2vy (first plane: video-range component Y’CbCr 8-bit 4:2:2, ordered Cb Y’0 Cr Y’1; second plane: alpha 8-bit) buffer.
- [var kvImage422CrYpCbYpCbYpCbYpCrYpCrYp10: vImageYpCbCrType](kvimage422crypcbypcbypcbypcrypcryp10.md)
  Any v210 (component Y’CbCr 10-bit 4:2:2) buffer.
- [var kvImage422YpCbYpCr8: vImageYpCbCrType](kvimage422ypcbypcr8.md)
  Any yuvs or yuvf (component Y’CbCr 8-bit 4:2:2, ordered Y’0 Cb Y’1 Cr) buffer.
- [var kvImage444AYpCbCr16: vImageYpCbCrType](kvimage444aypcbcr16.md)
  Any y416 (component Y’CbCrA 16-bit 4:4:4:4, ordered A Y’ Cb Cr, full range alpha, video range Y’CbCr) buffer.
- [var kvImage444AYpCbCr8: vImageYpCbCrType](kvimage444aypcbcr8.md)
  Any r408 or y408 (component Y’CbCrA 8-bit 4:4:4:4, ordered A Y’ Cb Cr, full range alpha, video range Y’CbCr) buffer.
- [var kvImage444CbYpCrA8: vImageYpCbCrType](kvimage444cbypcra8.md)
  Any v408 (component Y’CbCrA 8-bit 4:4:4:4) buffer.
- [var kvImage444CrYpCb10: vImageYpCbCrType](kvimage444crypcb10.md)
  Any v410 (component Y’CbCr 10-bit 4:4:4) buffer.
- [var kvImage444CrYpCb8: vImageYpCbCrType](kvimage444crypcb8.md)
  Any v308 (component Y’CbCr 8-bit 4:4:4) buffer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageConvert_ARGBToYpCbCr_GenerateConversion(UnsafePointer<vImage_ARGBToYpCbCrMatrix>, UnsafePointer<vImage_YpCbCrPixelRange>, UnsafeMutablePointer<vImage_ARGBToYpCbCr>, vImageARGBType, vImageYpCbCrType, vImage_Flags) -> vImage_Error](vimageconvert_argbtoypcbcr_generateconversion(_:_:_:_:_:_:).md)
  Generates the information that describes the conversion from ARGB to YpCbCr.
- [struct vImageARGBType](vimageargbtype.md)
  Constants that describe the encoding of an ARGB image for conversions between RGB and YpCbCr.
- [struct vImage_ARGBToYpCbCrMatrix](vimage_argbtoypcbcrmatrix.md)
  The 3 x 3 matrix that the vImage library uses to convert from RGB to YpCbCr.
- [struct vImage_ARGBToYpCbCr](vimage_argbtoypcbcr.md)
  The information that describes the conversion from ARGB to YpCbCr.
- [struct vImage_YpCbCrPixelRange](vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageypcbcrtype)*