# getWhite(_:alpha:)

**Framework**: UIKit  
**Kind**: method

Returns the grayscale components of the color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the color could be converted, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

If the color is in a compatible color space, it converts into grayscale format and its returned to your application. If the color isn’t in a compatible color space, the parameters don’t change.

## Parameters

- `white`: On return, the grayscale component of the color object. On applications linked for iOS 10 or later, an extended range gray color space specifies the grayscale component and can have any value. Values between   and   are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between   and  .
- `alpha`: On return, the opacity component of the color object, specified as a value between   and  .

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
- [var linearExposure: CGFloat](uicolor/linearexposure.md)
  The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [var accessibilityName: String](uicolor/accessibilityname.md)
  A localized description of the color for accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/getwhite(_:alpha:))*