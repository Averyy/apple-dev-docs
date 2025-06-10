# vImage_ARGBToYpCbCrMatrix

**Framework**: Accelerate  
**Kind**: struct

The 3 x 3 matrix that the vImage library uses to convert from RGB to YpCbCr.

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
struct vImage_ARGBToYpCbCrMatrix
```

#### Overview

The vImage library uses this matrix to convert from RGB to YpCbCr using the following multiplication:

```None
        | Y' |   | R_Yp        G_Yp   B_Yp      |   | R |
        | Cb | = | R_Cb        G_Cb   B_Cb_R_Cr | * | G |
        | Cr |   | B_Cb_R_Cr   G_Cr   B_Cr      |   | B |
```

## Topics

### Creating a conversion matrix
- [init(R_Yp: Float, G_Yp: Float, B_Yp: Float, R_Cb: Float, G_Cb: Float, B_Cb_R_Cr: Float, G_Cr: Float, B_Cr: Float)](vimage_argbtoypcbcrmatrix/init(r_yp:g_yp:b_yp:r_cb:g_cb:b_cb_r_cr:g_cr:b_cr:).md)
  Creates a 3 x 3 matrix for converting RGB to Y’CbCr.
- [init()](vimage_argbtoypcbcrmatrix/init.md)
  Creates a 3 x 3 zero matrix for converting RGB to Y’CbCr.
### Conversion matrix elements
- [var R_Yp: Float](vimage_argbtoypcbcrmatrix/r_yp.md)
  The  value in the conversion matrix.
- [var G_Yp: Float](vimage_argbtoypcbcrmatrix/g_yp.md)
  The  value in the conversion matrix.
- [var B_Yp: Float](vimage_argbtoypcbcrmatrix/b_yp.md)
  The  value in the conversion matrix.
- [var R_Cb: Float](vimage_argbtoypcbcrmatrix/r_cb.md)
  The  value in the conversion matrix.
- [var G_Cb: Float](vimage_argbtoypcbcrmatrix/g_cb.md)
  The  value in the conversion matrix.
- [var B_Cb_R_Cr: Float](vimage_argbtoypcbcrmatrix/b_cb_r_cr.md)
  The  value in the conversion matrix.
- [var G_Cr: Float](vimage_argbtoypcbcrmatrix/g_cr.md)
  The  value in the conversion matrix.
- [var B_Cr: Float](vimage_argbtoypcbcrmatrix/b_cr.md)
  The  value in the conversion matrix.
### Conversion matrices
- [var kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2: UnsafePointer<vImage_ARGBToYpCbCrMatrix>!](kvimage_argbtoypcbcrmatrix_itu_r_709_2.md)
  RGB-to-Y’CbCr conversion matrix for ITU Recommendation BT.709-2.
- [var kvImage_ARGBToYpCbCrMatrix_ITU_R_601_4: UnsafePointer<vImage_ARGBToYpCbCrMatrix>!](kvimage_argbtoypcbcrmatrix_itu_r_601_4.md)
  RGB-to-Y’CbCr conversion matrix for ITU Recommendation BT.601-4.
### Type Properties
- [static let itu_R_601_4: vImage_ARGBToYpCbCrMatrix](vimage_argbtoypcbcrmatrix/itu_r_601_4.md)
- [static let itu_R_709_2: vImage_ARGBToYpCbCrMatrix](vimage_argbtoypcbcrmatrix/itu_r_709_2.md)

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
- [struct vImage_ARGBToYpCbCr](vimage_argbtoypcbcr.md)
  The information that describes the conversion from ARGB to YpCbCr.
- [struct vImage_YpCbCrPixelRange](vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_argbtoypcbcrmatrix)*