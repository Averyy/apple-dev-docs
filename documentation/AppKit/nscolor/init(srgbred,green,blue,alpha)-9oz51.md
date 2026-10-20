# init(srgbRed:green:blue:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object from the specified components in the sRGB colorspace.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(srgbRed red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithSRGBRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue alpha:(CGFloat) alpha;
```

#### Return Value

The color object.

#### Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `red`: The red component of the color object.
- `green`: The green component of the color object.
- `blue`: The blue component of the color object.
- `alpha`: The opacity value of the color object.

## See Also

### Related Documentation
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28devicehue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity value and HSB color space components.
### Creating a color using RGB components
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28displayp3red,green,blue,alpha%29.md)
  Creates a color object from the specified components in the Display P3 color space.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Creates a color object with the specified red, green, blue, and alpha channel values.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28calibratedred,green,blue,alpha%29.md)
  Creates a color object using the given opacity and RGB components.
- [init(deviceRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28devicered,green,blue,alpha%29.md)
  Creates a color object using the given opacity value and RGB components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(srgbred:green:blue:alpha:)-9oz51)*