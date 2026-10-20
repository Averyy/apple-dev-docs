# adobeRGB1998

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A color space object that represents an Adobe RGB (1998) color space.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var adobeRGB1998: NSColorSpace { get }
```

```objc
@property (class, strong, readonly) NSColorSpace * adobeRGB1998ColorSpace;
```

#### Return Value

The `NSColorSpace` object. This color-additive color space has red, green, blue, and alpha components.

#### Discussion

The Adobe RGB (1998) color space was designed to encompass most of the colors achievable on CMYK color printers, but by using RGB primary colors on a device such as the computer display. For more information on this color space, go to [http://www.adobe.com/digitalimag/adobergb.html](http://www.adobe.com/digitalimag/adobergb.html).

## See Also

### Getting a Named Color Space
- [class var deviceRGB: NSColorSpace](./devicergb.md)
  A color space object that represents a calibrated or device-dependent RGB color space.
- [class var genericRGB: NSColorSpace](./genericrgb.md)
  A color space object that represents a device-independent RGB color space.
- [class var deviceCMYK: NSColorSpace](./devicecmyk.md)
  A color space object that represents a calibrated or device-dependent CMYK color space.
- [class var genericCMYK: NSColorSpace](./genericcmyk.md)
  A color space object that represents a device-independent CMYK color space.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/adobergb1998)*