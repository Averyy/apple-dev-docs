# genericCMYK

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A color space object that represents a device-independent CMYK color space.

**Availability**:
- macOS

## Declaration

```swift
class var genericCMYK: NSColorSpace { get }
```

```objc
@property (class, strong, readonly) NSColorSpace * genericCMYKColorSpace;
```

## Return Value

The `NSColorSpace` object. This color space has cyan, magenta, yellow, black and alpha component.

## See Also

### Getting a Named Color Space
- [class var deviceRGB: NSColorSpace](./devicergb.md)
  A color space object that represents a calibrated or device-dependent RGB color space.
- [class var genericRGB: NSColorSpace](./genericrgb.md)
  A color space object that represents a device-independent RGB color space.
- [class var deviceCMYK: NSColorSpace](./devicecmyk.md)
  A color space object that represents a calibrated or device-dependent CMYK color space.
- [class var deviceGray: NSColorSpace](./devicegray.md)
  A color space object that represents a calibrated or device-dependent gray color space.
- [class var genericGray: NSColorSpace](./genericgray.md)
  A color space object that represents a device-independent gray color space.
- [class var sRGB: NSColorSpace](./srgb.md)
  A color space object that represents an sRGB color space.
- [class var extendedSRGB: NSColorSpace](./extendedsrgb.md)
  A color space object that represents an extended sRGB color space.
- [class var displayP3: NSColorSpace](./displayp3.md)
  A color space object that represents a P3 Display color space.
- [class var genericGamma22Gray: NSColorSpace](./genericgamma22gray.md)
  A color space object that represents a gray color space with a gamma value of 2.2.
- [class var extendedGenericGamma22Gray: NSColorSpace](./extendedgenericgamma22gray.md)
  A color space object that represents an extended gray color space with a gamma value of 2.2.
- [class var adobeRGB1998: NSColorSpace](./adobergb1998.md)
  A color space object that represents an Adobe RGB (1998) color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/genericcmyk)*