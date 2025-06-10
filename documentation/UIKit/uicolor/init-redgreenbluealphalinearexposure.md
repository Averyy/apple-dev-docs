# init(red:green:blue:alpha:linearExposure:)

**Framework**: UIKit  
**Kind**: init

Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)
```

## See Also

- [init(white: CGFloat, alpha: CGFloat)](uicolor/init(white:alpha:).md)
  Creates a color object using the specified opacity and grayscale values.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](uicolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object using the specified opacity and HSB color space component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](uicolor/init(red:green:blue:alpha:exposure:).md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(displayp3red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [init?(named: String)](uicolor/init(named:).md)
  Creates a color object using the information from the named asset.
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](uicolor/init(named:inbundle:compatiblewithtraitcollection:).md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(red:green:blue:alpha:linearexposure:))*