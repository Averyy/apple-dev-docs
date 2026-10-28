# init(calibratedWhite:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the given opacity and grayscale values.

**Availability**:
- macOS

## Declaration

```swift
init(calibratedWhite white: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithCalibratedWhite:(CGFloat) white alpha:(CGFloat) alpha;
```

## Return Value

The color object.

## Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `white`: The grayscale value of the color object.
- `alpha`: The opacity value of the color object.

## See Also

### Related Documentation
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getwhite%28_,alpha%29.md)
  Returns the grayscale and alpha values of the color.
### Creating a color using white components
- [init(white: CGFloat, alpha: CGFloat)](./init%28white,alpha%29.md)
  Creates a color object with the specified brightness and alpha channel values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](./init%28devicewhite,alpha%29.md)
  Creates a color object using the given opacity and grayscale values.
- [init(genericGamma22White: CGFloat, alpha: CGFloat)](./init%28genericgamma22white,alpha%29.md)
  Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(calibratedwhite:alpha:))*