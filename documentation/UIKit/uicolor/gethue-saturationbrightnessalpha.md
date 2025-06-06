# getHue(_:saturation:brightness:alpha:)

**Framework**: UIKit  
**Kind**: method

Returns the components that form the color in the HSB color space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getHue(_ hue: UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the color could be converted, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

If the color is in a compatible color space, it converts into the HSB color space, and its components return to your application. If the color isn’t in a compatible color space, the parameters don’t change.

## Parameters

- `hue`: On return, the hue component of the color object. On applications linked for iOS 10 or later, an extended range color space specifies the hue component and can have any value. Values between   and   are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between   and  .
- `saturation`: On return, the saturation component of the color object. On applications linked for iOS 10 or later, an extended range color space specifies and can have any value. Values between   and   are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between   and  .
- `brightness`: On return, the brightness component of the color object. On applications linked for iOS 10 or later, an extended range color space specifies the brightness component and can have any value. Values between   and   are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between   and  .
- `alpha`: On return, the opacity component of the color object, specified as a value between   and  .

## See Also

- [Determining color values with color spaces](determining-color-values-with-color-spaces.md)
  Change the system’s interpretation of a color value for display by selecting a color space.
- [var cgColor: CGColor](uicolor/cgcolor.md)
  The Quartz color that corresponds to the color object.
- [var ciColor: CIColor](uicolor/cicolor.md)
  The Core Image color that corresponds to the color object.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](uicolor/getred(_:green:blue:alpha:).md)
  Returns the components that form the color in the RGB color space.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](uicolor/getwhite(_:alpha:).md)
  Returns the grayscale components of the color.
- [var accessibilityName: String](uicolor/accessibilityname.md)
  A localized description of the color for accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/gethue(_:saturation:brightness:alpha:))*