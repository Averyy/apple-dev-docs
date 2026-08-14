# init(hue:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: init

Creates a color object with the specified hue, saturation, brightness, and alpha channel values.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)
```

#### Return Value

The color object.

#### Discussion

This method accepts extended color component values. If the component values are outside of the `0-1.0` range, the method creates a color in the extended range color space. This method is provided for easier reuse of code that uses [`UIColor`](https://developer.apple.com/documentation/uikit/uicolor) in iOS.

Where possible, it is preferable to specify the colorspace explicitly using the [`init(srgbRed:green:blue:alpha:)`](nscolor/init(srgbred:green:blue:alpha:)-9oz51.md) or [`init(genericGamma22White:alpha:)`](nscolor/init(genericgamma22white:alpha:).md) method.

## Parameters

- `hue`: The hue (color) component. If the value is outside of the range `0–1.0`, the extended range color space is used.
- `saturation`: The color saturation component. If the value is outside of the range `0–1.0`, the extended range color space is used.
- `brightness`: The brightness component. If the value is outside of the range `0–1.0`, the extended range color space is used.
- `alpha`: The alpha (opacity), specified as a value from `0-1.0`. Alpha values below `0` are interpreted as `0.0`, and values above `1.0` are interpreted as `1.0`.

## See Also

- [init(calibratedHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(calibratedhue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity and HSB color space components.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(devicehue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(colorSpace: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(colorspace:hue:saturation:brightness:alpha:).md)
  Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(hue:saturation:brightness:alpha:))*