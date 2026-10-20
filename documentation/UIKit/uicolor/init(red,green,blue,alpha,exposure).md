# init(red:green:blue:alpha:exposure:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)
```

```objc
- (UIColor *) initWithRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue alpha:(CGFloat) alpha exposure:(CGFloat) exposure;
```

## See Also

### Creating a color from component values
- [init(white: CGFloat, alpha: CGFloat)](./init%28white,alpha%29.md)
  Creates a color object using the specified opacity and grayscale values.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28hue,saturation,brightness,alpha%29.md)
  Creates a color object using the specified opacity and HSB color space component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Creates a color object using the specified opacity and RGB component values.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)](./init%28red,green,blue,alpha,linearexposure%29.md)
  Generates an HDR color by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28displayp3red,green,blue,alpha%29.md)
  Creates a color object using the specified opacity and RGB component values in the Display P3 color space.
- [init?(named: String)](./init%28named%29.md)
  Creates a color object using the information from the named asset.
- [init?(named: String, inBundle: Bundle?, compatibleWithTraitCollection: UITraitCollection?)](./init%28named,inbundle,compatiblewithtraitcollection%29.md)
  Creates a color object using the named asset that’s compatible with the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(red:green:blue:alpha:exposure:))*