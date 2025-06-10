# vImage_YpCbCrToARGBMatrix

**Framework**: Accelerate  
**Kind**: struct

The 3 x 3 matrix that the vImage library uses to convert from YpCbCr to RGB.

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
struct vImage_YpCbCrToARGBMatrix
```

#### Overview

The vImage library uses this matrix to convert from YpCbCr to RGB using the following multiplication:

```None
                    | R |   | Yp    0     Cr_R |   | Y' |
                    | G | = | Yp   Cb_G   Cr_G | * | Cb |
                    | B |   | Yp   Cb_B     0  |   | Cr |
```

## Topics

### Creating a conversion matrix
- [init(Yp: Float, Cr_R: Float, Cr_G: Float, Cb_G: Float, Cb_B: Float)](vimage_ypcbcrtoargbmatrix/init(yp:cr_r:cr_g:cb_g:cb_b:).md)
  Creates a 3 x 3 matrix for converting Y’CbCr signals to RGB.
- [init()](vimage_ypcbcrtoargbmatrix/init.md)
  Creates a 3 x 3 zero matrix for converting Y’CbCr signals to RGB.
### Conversion matrix elements
- [var Yp: Float](vimage_ypcbcrtoargbmatrix/yp.md)
  The  value in the conversion matrix.
- [var Cr_R: Float](vimage_ypcbcrtoargbmatrix/cr_r.md)
  The  value in the conversion matrix.
- [var Cr_G: Float](vimage_ypcbcrtoargbmatrix/cr_g.md)
  The  value in the conversion matrix.
- [var Cb_G: Float](vimage_ypcbcrtoargbmatrix/cb_g.md)
  The  value in the conversion matrix.
- [var Cb_B: Float](vimage_ypcbcrtoargbmatrix/cb_b.md)
  The  value in the conversion matrix.
### Conversion matrices
- [var kvImage_YpCbCrToARGBMatrix_ITU_R_601_4: UnsafePointer<vImage_YpCbCrToARGBMatrix>!](kvimage_ypcbcrtoargbmatrix_itu_r_601_4.md)
  Y’CbCr-to-RGB conversion matrix for ITU Recommendation BT.601-4.
- [var kvImage_YpCbCrToARGBMatrix_ITU_R_709_2: UnsafePointer<vImage_YpCbCrToARGBMatrix>!](kvimage_ypcbcrtoargbmatrix_itu_r_709_2.md)
  Y’CbCr-to-RGB conversion matrix for ITU Recommendation BT.709-2.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageConvert_YpCbCrToARGB_GenerateConversion(UnsafePointer<vImage_YpCbCrToARGBMatrix>, UnsafePointer<vImage_YpCbCrPixelRange>, UnsafeMutablePointer<vImage_YpCbCrToARGB>, vImageYpCbCrType, vImageARGBType, vImage_Flags) -> vImage_Error](vimageconvert_ypcbcrtoargb_generateconversion(_:_:_:_:_:_:).md)
  Generates the information that describes the conversion from YpCbCr to ARGB.
- [struct vImageYpCbCrType](vimageypcbcrtype.md)
  Constants that describe the encoding of a YpCbCr image for conversions between RGB and YpCbCr.
- [struct vImageARGBType](vimageargbtype.md)
  Constants that describe the encoding of an ARGB image for conversions between RGB and YpCbCr.
- [struct vImage_YpCbCrToARGB](vimage_ypcbcrtoargb.md)
  The information that describes the conversion from YpCbCr to ARGB.
- [struct vImage_YpCbCrPixelRange](vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrtoargbmatrix)*