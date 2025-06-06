# yCbCrMatrix

**Framework**: Core Graphics  
**Kind**: property

This key should only be included if you the display stream is creating output frames in either the 420v or 420f formats. It is used to specify the YCbCr matrix applied to the output surface.

## Declaration

```swift
class let yCbCrMatrix: CFString
```

#### Discussion

The value associated with this key must be one of the strings specified in [`Display Stream YCbCr to RGB conversion Matrix Options`](display-stream-ycbcr-to-rgb-conversion-matrix-options.md).

## See Also

- [class let colorSpace: CFString](cgdisplaystream/colorspace.md)
  This key specifies the color space of the output buffer. If this key is not included in the dictionary, the output buffer uses the same color space as the display. The value associated with this key must be a [`CGColorSpace`](cgcolorspace.md) for the desired color space.
- [class let conversionBlackPointCompensation: CFString](cgcolor/conversionblackpointcompensation.md)
  An option for whether to apply black point compensation when converting between color profiles.
- [var kCGDisplayBitsPerPixel: String](kcgdisplaybitsperpixel.md)
  Specifies a CFNumber integer value that represents the number of bits in a pixel.
- [var kCGDisplayBitsPerSample: String](kcgdisplaybitspersample.md)
  Specifies a CFNumber integer value that represents the number of bits in an individual sample (for example, a color value in an RGB pixel).
- [var kCGDisplayBlendNormal: Double](kcgdisplayblendnormal.md)
  The blend color is not applied at the start or end of a fade operation.
- [var kCGDisplayBlendSolidColor: Double](kcgdisplayblendsolidcolor.md)
  The user sees only the blend color at the start or end of a fade operation.
- [var kCGDisplayBytesPerRow: String](kcgdisplaybytesperrow.md)
  Specifies a CFNumber integer value that represents the number of bytes in a row on the display.
- [var kCGDisplayFadeReservationInvalidToken: Int32](kcgdisplayfadereservationinvalidtoken.md)
- [var kCGDisplayHeight: String](kcgdisplayheight.md)
  Specifies a CFNumber integer value that represents the height of the display in pixels.
- [var kCGDisplayIOFlags: String](kcgdisplayioflags.md)
  Specifies a CFNumber integer value that contains the I/O Kit display mode flags. For more information, see the header file `IOKit/IOGraphicsTypes.h`.
- [var kCGDisplayMode: String](kcgdisplaymode.md)
  Specifies a `CFNumber` integer value that represents the I/O Kit display mode number.
- [var kCGDisplayModeIsInterlaced: String](kcgdisplaymodeisinterlaced.md)
  Specifies a CFBoolean value indicating that the I/O Kit interlace mode flag is set.
- [var kCGDisplayModeIsSafeForHardware: String](kcgdisplaymodeissafeforhardware.md)
  Specifies a CFBoolean value indicating that the display mode doesn’t need a confirmation dialog to be set.
- [var kCGDisplayModeIsStretched: String](kcgdisplaymodeisstretched.md)
  Specifies a CFBoolean value indicating that the I/O Kit stretched mode flag is set.
- [var kCGDisplayModeIsTelevisionOutput: String](kcgdisplaymodeistelevisionoutput.md)
  Specifies a CFBoolean value indicating that the I/O Kit television output mode flag is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/ycbcrmatrix)*