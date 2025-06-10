# accessibilityName

**Framework**: UIKit  
**Kind**: property

A localized description of the color for accessibility attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var accessibilityName: String { get }
```

## See Also

- [Determining color values with color spaces](determining-color-values-with-color-spaces.md)
  Change the system’s interpretation of a color value for display by selecting a color space.
- [var cgColor: CGColor](uicolor/cgcolor.md)
  The Quartz color that corresponds to the color object.
- [var ciColor: CIColor](uicolor/cicolor.md)
  The Core Image color that corresponds to the color object.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](uicolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the components that form the color in the HSB color space.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](uicolor/getred(_:green:blue:alpha:).md)
  Returns the components that form the color in the RGB color space.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](uicolor/getwhite(_:alpha:).md)
  Returns the grayscale components of the color.
- [var linearExposure: CGFloat](uicolor/linearexposure.md)
  The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/accessibilityname)*