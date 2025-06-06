# init(colorSpace:hue:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: init

Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.

**Availability**:
- macOS 10.12+

## Declaration

```swift
init(colorSpace space: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)
```

#### Return Value

The color object.

## Parameters

- `space`: An   object representing a color space. An exception is raised if the color model of the provided color space is not RGB.
- `hue`: The hue (color) component, expressed as a floating-point value in the range 0–1.0.
- `saturation`: The color saturation component, expressed as a floating-point value in the range 0–1.0.
- `brightness`: The brightness component, expressed as a floating-point value in the range 0–1.0.
- `alpha`: The alpha (opacity), expressed as a floating-point value in the range 0 (transparent) to 1.0 (opaque).

## See Also

- [init(calibratedHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(calibratedhue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity and HSB color space components.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(devicehue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object with the specified hue, saturation, brightness, and alpha channel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(colorspace:hue:saturation:brightness:alpha:))*