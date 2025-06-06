# init(white:alpha:)

**Framework**: AppKit  
**Kind**: init

Creates a color object with the specified brightness and alpha channel values.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init(white: CGFloat, alpha: CGFloat)
```

#### Discussion

This method accepts extended color component values. If the alpha or white values are outside of the `0-1.0` range, the method creates a color in the extended range or [`extendedGenericGamma22Gray`](nscolorspace/extendedgenericgamma22gray.md) color space that is compatible with the sRGB colorspace. This method is provided for easier reuse of code that uses [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) in iOS.

Where possible, it is preferable to specify the colorspace explicitly using the [`init(srgbRed:green:blue:alpha:)`](nscolor/init(srgbred:green:blue:alpha:).md) or [`init(genericGamma22White:alpha:)`](nscolor/init(genericgamma22white:alpha:).md) method.

## Parameters

- `white`: The brightness. If the value is outside of the range  , the extended sRGB color space is used.
- `alpha`: The alpha (opacity), expressed as a floating-point value in the range   (transparent) to   (opaque). Alpha values below   are interpreted as  , and values above   are interpreted as  .

## See Also

- [init(calibratedWhite: CGFloat, alpha: CGFloat)](nscolor/init(calibratedwhite:alpha:).md)
  Creates a color object using the given opacity and grayscale values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](nscolor/init(devicewhite:alpha:).md)
  Creates a color object using the given opacity and grayscale values.
- [init(genericGamma22White: CGFloat, alpha: CGFloat)](nscolor/init(genericgamma22white:alpha:).md)
  Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(white:alpha:))*