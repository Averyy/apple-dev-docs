# init(calibratedHue:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the given opacity and HSB color space components.

**Availability**:
- macOS

## Declaration

```swift
init(calibratedHue hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithCalibratedHue:(CGFloat) hue saturation:(CGFloat) saturation brightness:(CGFloat) brightness alpha:(CGFloat) alpha;
```

#### Return Value

The color object.

#### Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `hue`: The hue component of the color object in the HSB color space.
- `saturation`: The saturation component of the color object in the HSB color space.
- `brightness`: The brightness (or value) component of the color object in the HSB color space.
- `alpha`: The opacity value of the color object,

## See Also

### Related Documentation
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28calibratedred,green,blue,alpha%29.md)
  Creates a color object using the given opacity and RGB components.
### Creating a color using HSB components
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28devicehue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28hue,saturation,brightness,alpha%29.md)
  Creates a color object with the specified hue, saturation, brightness, and alpha channel values.
- [init(colorSpace: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28colorspace,hue,saturation,brightness,alpha%29.md)
  Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(calibratedhue:saturation:brightness:alpha:))*