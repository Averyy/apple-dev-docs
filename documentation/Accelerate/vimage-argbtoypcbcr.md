# vImage_ARGBToYpCbCr

**Framework**: Accelerate  
**Kind**: struct

The information that describes the conversion from ARGB to YpCbCr.

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
struct vImage_ARGBToYpCbCr
```

## Topics

### Raw Values
- [init()](vimage_argbtoypcbcr/init.md)
- [init(opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](vimage_argbtoypcbcr/init(opaque:).md)
- [var opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](vimage_argbtoypcbcr/opaque.md)

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
- [struct vImage_YpCbCrPixelRange](vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_argbtoypcbcr)*