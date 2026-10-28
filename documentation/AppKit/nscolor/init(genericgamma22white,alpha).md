# init(genericGamma22White:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(genericGamma22White white: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithGenericGamma22White:(CGFloat) white alpha:(CGFloat) alpha;
```

## Return Value

The color object.

## Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `white`: The white value of the color object.
- `alpha`: The opacity value of the color object.

## See Also

### Related Documentation
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28srgbred,green,blue,alpha%29-9oz51.md)
  Creates a color object from the specified components in the sRGB colorspace.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./init%28devicehue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28calibratedred,green,blue,alpha%29.md)
  Creates a color object using the given opacity and RGB components.
### Creating a color using white components
- [init(white: CGFloat, alpha: CGFloat)](./init%28white,alpha%29.md)
  Creates a color object with the specified brightness and alpha channel values.
- [init(calibratedWhite: CGFloat, alpha: CGFloat)](./init%28calibratedwhite,alpha%29.md)
  Creates a color object using the given opacity and grayscale values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](./init%28devicewhite,alpha%29.md)
  Creates a color object using the given opacity and grayscale values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(genericgamma22white:alpha:))*