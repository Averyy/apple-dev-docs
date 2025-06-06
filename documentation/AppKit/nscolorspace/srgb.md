# sRGB

**Framework**: AppKit  
**Kind**: property

A color space object that represents an sRGB color space.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var sRGB: NSColorSpace { get }
```

#### Return Value

The `NSColorSpace` object. This color-additive color space has red, green, blue, and alpha components.

#### Discussion

The sRGB color space is a standard color space for use on monitors, printers, and the Internet. For further information on sRGB, see [`http://www.color.org/srgb.html`](https://developer.apple.comhttp://www.color.org/srgb.html).

## See Also

- [class var deviceRGB: NSColorSpace](nscolorspace/devicergb.md)
  A color space object that represents a calibrated or device-dependent RGB color space.
- [class var genericRGB: NSColorSpace](nscolorspace/genericrgb.md)
  A color space object that represents a device-independent RGB color space.
- [class var deviceCMYK: NSColorSpace](nscolorspace/devicecmyk.md)
  A color space object that represents a calibrated or device-dependent CMYK color space.
- [class var genericCMYK: NSColorSpace](nscolorspace/genericcmyk.md)
  A color space object that represents a device-independent CMYK color space.
- [class var deviceGray: NSColorSpace](nscolorspace/devicegray.md)
  A color space object that represents a calibrated or device-dependent gray color space.
- [class var genericGray: NSColorSpace](nscolorspace/genericgray.md)
  A color space object that represents a device-independent gray color space.
- [class var extendedSRGB: NSColorSpace](nscolorspace/extendedsrgb.md)
  A color space object that represents an extended sRGB color space.
- [class var displayP3: NSColorSpace](nscolorspace/displayp3.md)
  A color space object that represents a P3 Display color space.
- [class var genericGamma22Gray: NSColorSpace](nscolorspace/genericgamma22gray.md)
  A color space object that represents a gray color space with a gamma value of 2.2.
- [class var extendedGenericGamma22Gray: NSColorSpace](nscolorspace/extendedgenericgamma22gray.md)
  A color space object that represents an extended gray color space with a gamma value of 2.2.
- [class var adobeRGB1998: NSColorSpace](nscolorspace/adobergb1998.md)
  A color space object that represents an Adobe RGB (1998) color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/srgb)*