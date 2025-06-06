# init(red:green:blue:alpha:)

**Framework**: AppKit  
**Kind**: init

Creates a color object with the specified red, green, blue, and alpha channel values.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

#### Discussion

This method accepts extended color component values. If the red, green, blue, or alpha values are outside of the `0-1.0` range, the method creates a color in the extended range color space. This method is provided for easier reuse of code that uses [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) in iOS.

Where possible, it is preferable to specify the colorspace explicitly using the [`init(srgbRed:green:blue:alpha:)`](nscolor/init(srgbred:green:blue:alpha:).md) or [`init(genericGamma22White:alpha:)`](nscolor/init(genericgamma22white:alpha:).md) method.

## Parameters

- `red`: The red channel value. If the value is outside of the range  , the extended sRGB color space is used.
- `green`: The green channel value. If the value is outside of the range  , the extended sRGB color space is used.
- `blue`: The blue channel value. If the value is outside of the range  , the extended sRGB color space is used.
- `alpha`: The alpha (opacity), specified as a value from  . Alpha values below   are interpreted as  , and values above   are interpreted as  .

## See Also

- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(srgbred:green:blue:alpha:).md)
  Creates a color object from the specified components in the sRGB colorspace.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(displayp3red:green:blue:alpha:).md)
  Creates a color object from the specified components in the Display P3 color space.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(calibratedred:green:blue:alpha:).md)
  Creates a color object using the given opacity and RGB components.
- [init(deviceRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(devicered:green:blue:alpha:).md)
  Creates a color object using the given opacity value and RGB components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(red:green:blue:alpha:))*