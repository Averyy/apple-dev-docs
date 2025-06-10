# init(named:inBundle:compatibleWithTraitCollection:)

**Framework**: UIKit  
**Kind**: init

Creates a color object using the named asset that’s compatible with the specified trait collection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(named name: String, in bundle: Bundle?, compatibleWith traitCollection: UITraitCollection?)
```

#### Return Value

An initialized color object. The returned object uses the color space specified for the asset.

## Parameters

- `name`: The name of the asset containing the color.
- `bundle`: The bundle containing the asset.
- `traitCollection`: The trait collection that specifies the gamut to use when selecting the color.

## See Also

- [init(white: CGFloat, alpha: CGFloat)](uicolor/init(white:alpha:).md)
  Creates a color object using the specified opacity and grayscale values.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](uicolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object using the specified opacity and HSB color space component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](uicolor/init(red:green:blue:alpha:exposure:).md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)](uicolor/init(red:green:blue:alpha:linearexposure:).md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(displayp3red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [init?(named: String)](uicolor/init(named:).md)
  Creates a color object using the information from the named asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(named:inbundle:compatiblewithtraitcollection:))*