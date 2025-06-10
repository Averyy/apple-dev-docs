# Color creation

**Framework**: UIKit

Load colors from asset catalogs and create colors from raw component values.

#### Overview

Create color objects when you want to use specific colors in your UI, altering the raw component values used by grayscale, RGB, HSB, and CMYK. You can set the specified opacity and RGB component values to create personalized colors that fit your needs. Create colors dynamically by component values changing based on the currently active traits. You can use pattern colors to set the fill or stroke color.

## Topics

### Creating a color from component values
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
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](uicolor/init(named:inbundle:compatiblewithtraitcollection:).md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.
### Creating a color dynamically
- [init(dynamicProvider: (UITraitCollection) -> UIColor)](uicolor/init(dynamicprovider:).md)
  Creates a color object that uses the specified block to generate its color data dynamically.
### Creating a color from another color object
- [convenience init(Color)](uicolor/init(_:).md)
  Creates a color object that encapsulates a SwiftUI color.
- [init(ciColor: CIColor)](uicolor/init(cicolor:).md)
  Creates a color object that encapsulates a Core Image color.
- [init(cgColor: CGColor)](uicolor/init(cgcolor:).md)
  Creates a color object using the specified Quartz color reference.
- [func withAlphaComponent(CGFloat) -> UIColor](uicolor/withalphacomponent(_:).md)
  Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
### Creating a pattern-based color
- [init(patternImage: UIImage)](uicolor/init(patternimage:).md)
  Creates a color object using the specified image object.
### Creating a color from a resource
- [convenience init(resource: ColorResource)](uicolor/init(resource:).md)

## See Also

- [UI element colors](ui-element-colors.md)
  Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Standard colors](standard-colors.md)
  Define standard color objects for specific shades, such as red, blue, green, black, white, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/color-creation)*