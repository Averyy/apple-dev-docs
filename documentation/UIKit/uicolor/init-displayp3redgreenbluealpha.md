# init(displayP3Red:green:blue:alpha:)

**Framework**: UIKit  
**Kind**: init

Creates a color object using the specified opacity and RGB component values in the Display P3 color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

#### Return Value

The color object. The color information represented by this object is in an extended range sRGB colorspace. On applications linked for iOS 10 or later, the color is specified in an extended range sRGB color space.

#### Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `displayP3Red`: The red component of the color object, specified as a value from 0.0 to 1.0.
- `green`: The green component of the color object, specified as a value from 0.0 to 1.0.
- `blue`: The blue component of the color object, specified as a value from 0.0 to 1.0.
- `alpha`: The opacity value of the color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## See Also

- [init(white: CGFloat, alpha: CGFloat)](uicolor/init(white:alpha:).md)
  Creates a color object using the specified opacity and grayscale values.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](uicolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object using the specified opacity and HSB color space component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](uicolor/init(red:green:blue:alpha:).md)
  Creates a color object using the specified opacity and RGB component values.
- [init?(named: String)](uicolor/init(named:).md)
  Creates a color object using the information from the named asset.
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](uicolor/init(named:inbundle:compatiblewithtraitcollection:).md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(displayp3red:green:blue:alpha:))*