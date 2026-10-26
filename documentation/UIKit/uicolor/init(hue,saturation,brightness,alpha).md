# init(hue:saturation:brightness:alpha:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the specified opacity and HSB color space component values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)
```

```objc
- (UIColor *) initWithHue:(CGFloat) hue saturation:(CGFloat) saturation brightness:(CGFloat) brightness alpha:(CGFloat) alpha;
```

#### Return Value

The color object. The color information represented by this object is in an RGB colorspace. On applications linked for iOS 10 or later, the color is specified in an extended range sRGB color space. On earlier versions of iOS, the color is specified in a device RGB colorspace.

## Parameters

- `hue`: The hue value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, hue values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `saturation`: The saturation value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, saturation values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `brightness`: The brightness value of the color object. On applications linked for iOS 10 or later, the color is specified in an extended color space, and the input value is never clamped. On earlier versions of iOS, brightness values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.
- `alpha`: The opacity value of the color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## See Also

### Creating a color from component values
- [init(white: CGFloat, alpha: CGFloat)](./init%28white,alpha%29.md)
  Creates a color object using the specified opacity and grayscale values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Creates a color object using the specified opacity and RGB component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](./init%28red,green,blue,alpha,exposure%29.md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)](./init%28red,green,blue,alpha,linearexposure%29.md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28displayp3red,green,blue,alpha%29.md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [init?(named: String)](./init%28named%29.md)
  Creates a color object using the information from the named asset.
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](./init%28named,inbundle,compatiblewithtraitcollection%29.md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.
- [+ colorWithWhite:alpha:](./colorwithwhite_alpha_.md)
  Creates a color object using the specified opacity and grayscale values.
- [+ colorWithRed:green:blue:alpha:](./colorwithred_green_blue_alpha_.md)
  Creates a color object using the specified opacity and RGB component values.
- [+ colorWithDisplayP3Red:green:blue:alpha:](./colorwithdisplayp3red_green_blue_alpha_.md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
### Related Documentation
- [+ colorWithHue:saturation:brightness:alpha:](./colorwithhue_saturation_brightness_alpha_.md)
  Creates a color object using the specified opacity and HSB color space component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(hue:saturation:brightness:alpha:))*