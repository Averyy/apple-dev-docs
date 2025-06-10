# init(red:green:blue:alpha:)

**Framework**: UIKit  
**Kind**: init

Creates a color object using the specified opacity and RGB component values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

#### Return Value

The color object. The color information represented by this object is in an RGB colorspace. On applications linked for iOS 10 or later, the color is specified in an extended range sRGB color space. On earlier versions of iOS, the color is specified in a device RGB colorspace.

## Parameters

- `red`: The red value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, red values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `green`: The green value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, green values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `blue`: The blue value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, blue values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `alpha`: The opacity value of the color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## See Also

- [init(white: CGFloat, alpha: CGFloat)](uicolor/init(white:alpha:).md)
  Creates a color object using the specified opacity and grayscale values.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](uicolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object using the specified opacity and HSB color space component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](uicolor/init(red:green:blue:alpha:exposure:).md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)](uicolor/init(red:green:blue:alpha:linearexposure:).md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(displayp3red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [init?(named: String)](uicolor/init(named:).md)
  Creates a color object using the information from the named asset.
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](uicolor/init(named:inbundle:compatiblewithtraitcollection:).md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(red:green:blue:alpha:))*