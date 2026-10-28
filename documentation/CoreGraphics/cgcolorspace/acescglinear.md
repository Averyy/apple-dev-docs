# acescgLinear

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

The ACEScg color space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let acescgLinear: CFString
```

```c
extern CFStringRef const kCGColorSpaceACESCGLinear;
```

## Discussion

For more information, see “ACEScg—A Working Space for CGI Render and Compositing”, Version 1.0.1, Academy of Motion Picture Arts and Sciences ([http://www.oscars.org/science-technology/sci-tech-projects/aces](http://www.oscars.org/science-technology/sci-tech-projects/aces)).

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/acescglinear)*