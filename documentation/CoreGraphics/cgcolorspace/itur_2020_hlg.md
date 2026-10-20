# itur_2020_HLG

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the HLG transfer function.

**Availability**:
- iOS 12.6+ - Deprecated in 14.0
- iPadOS 12.6+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.15.6+ - Deprecated in 11.0
- tvOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 7.0

> **Deprecated**: No longer supported

## Declaration

```swift
class let itur_2020_HLG: CFString
```

```c
extern CFStringRef const kCGColorSpaceITUR_2020_HLG;
```

#### Discussion

This color space has the same colorimetry as [`itur_2020`](./itur_2020.md), but uses the Hybrid Log-Gamma (HLG) transfer function. Pixel values should be between `0.0` and `12.0`. See the current active version of the BT.2100 recommendation on the ITU website ([https://www.itu.int/](https://www.itu.int/)).

## See Also

### Accessing System-Defined Color Spaces
- [class let displayP3: CFString](./displayp3.md)
  The Display P3 color space, created by Apple.
- [class let displayP3_HLG: CFString](./displayp3_hlg.md)
  The Display P3 color space, using the HLG transfer function.
- [class let displayP3_PQ_EOTF: CFString](./displayp3_pq_eotf.md)
  The Display P3 color space, using the PQ transfer function.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/itur_2020_hlg)*