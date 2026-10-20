# displayP3_PQ_EOTF

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

The Display P3 color space, using the PQ transfer function.

**Availability**:
- iOS 12.6+ - Deprecated in 13.4
- iPadOS 12.6+ - Deprecated in 13.4
- Mac Catalyst 13.1+ - Deprecated in 13.4
- macOS 10.14.6+ - Deprecated in 10.15.4
- tvOS 12.0+ - Deprecated in 13.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 6.2

> **Deprecated**: No longer supported

## Declaration

```swift
class let displayP3_PQ_EOTF: CFString
```

```c
extern CFStringRef const kCGColorSpaceDisplayP3_PQ_EOTF;
```

#### Discussion

This color space was created by Apple Inc. This color space uses the DCI P3 primaries, a D65 white point, and the Perceptual Quantizer (PQ) transfer function. For more information on PQ, see [https://www.itu.int/rec/R-REC-BT.2100](https://www.itu.int/rec/R-REC-BT.2100).

## See Also

### Accessing System-Defined Color Spaces
- [class let displayP3: CFString](./displayp3.md)
  The Display P3 color space, created by Apple.
- [class let displayP3_HLG: CFString](./displayp3_hlg.md)
  The Display P3 color space, using the HLG transfer function.
- [class let extendedLinearDisplayP3: CFString](./extendedlineardisplayp3.md)
  The Display P3 color space with a linear transfer function and extended-range values.
- [class let sRGB: CFString](./srgb.md)
  The standard Red Green Blue (sRGB) color space.
- [class let linearSRGB: CFString](./linearsrgb.md)
  The sRGB color space with a linear transfer function.
- [class let extendedSRGB: CFString](./extendedsrgb.md)
  The extended sRGB color space.
- [class let extendedLinearSRGB: CFString](./extendedlinearsrgb.md)
  The sRGB color space with a linear transfer function and extended-range values.
- [class let genericGrayGamma2_2: CFString](./genericgraygamma2_2.md)
  The generic gray color space that has an exponential transfer function with a power of 2.2.
- [class let extendedGray: CFString](./extendedgray.md)
  The extended gray color space.
- [class let linearGray: CFString](./lineargray.md)
  The gray color space using a linear transfer function.
- [class let extendedLinearGray: CFString](./extendedlineargray.md)
  The extended gray color space with a linear transfer function.
- [class let genericCMYK: CFString](./genericcmyk.md)
  The generic CMYK color space.
- [class let genericRGBLinear: CFString](./genericrgblinear.md)
  The generic RGB color space with a linear transfer function.
- [class let genericXYZ: CFString](./genericxyz.md)
  The XYZ color space, as defined by the CIE 1931 standard.
- [class let genericLab: CFString](./genericlab.md)
  The generic LAB color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/displayp3_pq_eotf)*