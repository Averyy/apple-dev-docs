# init(colorSpace:hue:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.

**Availability**:
- macOS 10.12+

## Declaration

```swift
init(colorSpace space: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithColorSpace:(NSColorSpace *) space hue:(CGFloat) hue saturation:(CGFloat) saturation brightness:(CGFloat) brightness alpha:(CGFloat) alpha;
```

## Return Value

The color object.

## Parameters

- `space`: An `NSColorSpace` object representing a color space. An exception is raised if the color model of the provided color space is not RGB.
- `hue`: The hue (color) component, expressed as a floating-point value in the range 0–1.0.
- `saturation`: The color saturation component, expressed as a floating-point value in the range 0–1.0.
- `brightness`: The brightness component, expressed as a floating-point value in the range 0–1.0.
- `alpha`: The alpha (opacity), expressed as a floating-point value in the range 0 (transparent) to 1.0 (opaque).

## See Also

### Creating a color using HSB components
- [init(calibratedHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28calibratedhue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity and HSB color space components.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28devicehue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28hue,saturation,brightness,alpha%29.md)
  Creates a color object with the specified hue, saturation, brightness, and alpha channel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(colorspace:hue:saturation:brightness:alpha:))*