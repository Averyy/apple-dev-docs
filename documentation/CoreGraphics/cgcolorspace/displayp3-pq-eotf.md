# displayP3_PQ_EOTF

**Framework**: Core Graphics  
**Kind**: property

The Display P3 color space, using the PQ transfer function.

**Availability**:
- iOS 12.6+
- iPadOS 12.6+
- Mac Catalyst 13.1+
- macOS 10.14.6+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class let displayP3_PQ_EOTF: CFString
```

#### Discussion

This color space was created by Apple Inc. This color space uses the DCI P3 primaries, a D65 white point, and the Perceptual Quantizer (PQ) transfer function. For more information on PQ, see [`https://www.itu.int/rec/R-REC-BT.2100`](https://developer.apple.comhttps://www.itu.int/rec/R-REC-BT.2100).

## See Also

- [class let displayP3: CFString](cgcolorspace/displayp3.md)
  The Display P3 color space, created by Apple.
- [class let displayP3_HLG: CFString](cgcolorspace/displayp3_hlg.md)
  The Display P3 color space, using the HLG transfer function.
- [class let extendedLinearDisplayP3: CFString](cgcolorspace/extendedlineardisplayp3.md)
  The Display P3 color space with a linear transfer function and extended-range values.
- [class let sRGB: CFString](cgcolorspace/srgb.md)
  The standard Red Green Blue (sRGB) color space.
- [class let linearSRGB: CFString](cgcolorspace/linearsrgb.md)
  The sRGB color space with a linear transfer function.
- [class let extendedSRGB: CFString](cgcolorspace/extendedsrgb.md)
  The extended sRGB color space.
- [class let extendedLinearSRGB: CFString](cgcolorspace/extendedlinearsrgb.md)
  The sRGB color space with a linear transfer function and extended-range values.
- [class let genericGrayGamma2_2: CFString](cgcolorspace/genericgraygamma2_2.md)
  The generic gray color space that has an exponential transfer function with a power of 2.2.
- [class let extendedGray: CFString](cgcolorspace/extendedgray.md)
  The extended gray color space.
- [class let linearGray: CFString](cgcolorspace/lineargray.md)
  The gray color space using a linear transfer function.
- [class let extendedLinearGray: CFString](cgcolorspace/extendedlineargray.md)
  The extended gray color space with a linear transfer function.
- [class let genericCMYK: CFString](cgcolorspace/genericcmyk.md)
  The generic CMYK color space.
- [class let genericRGBLinear: CFString](cgcolorspace/genericrgblinear.md)
  The generic RGB color space with a linear transfer function.
- [class let genericXYZ: CFString](cgcolorspace/genericxyz.md)
  The XYZ color space, as defined by the CIE 1931 standard.
- [class let genericLab: CFString](cgcolorspace/genericlab.md)
  The generic LAB color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/displayp3_pq_eotf)*