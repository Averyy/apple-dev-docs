# deviceRGB

**Framework**: AppKit  
**Kind**: property

A color space object that represents a calibrated or device-dependent RGB color space.

**Availability**:
- macOS ?+

## Declaration

```swift
class var deviceRGB: NSColorSpace { get }
```

#### Return Value

The `NSColorSpace` object. This color space has red, green, blue, and alpha components. Typical devices that use the color-additive RGB color space are displays and scanners. This object corresponds to the Cocoa color space name `NSDeviceRGBColorSpace`.

## See Also

- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)
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
- [class var sRGB: NSColorSpace](nscolorspace/srgb.md)
  A color space object that represents an sRGB color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/devicergb)*