# getRed(_:green:blue:alpha:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the components that form the color in the RGB color space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getRed(_ red: UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool
```

```objc
- (BOOL) getRed:(CGFloat *) red green:(CGFloat *) green blue:(CGFloat *) blue alpha:(CGFloat *) alpha;
```

#### Return Value

[`true`](../../Swift/true.md) if the color could be converted, [`false`](../../Swift/false.md) otherwise.

#### Discussion

If the color is in a compatible color space, it converts into RGB format and its components return to your application. If the color isn’t in a compatible color space, the parameters don’t change.

## Parameters

- `red`: On return, the red component of the color object. On applications linked for iOS 10 or later, an extended range sRGB color space specifies the red component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.
- `green`: On return, the green component of the color object. On applications linked for iOS 10 or later,an extended range sRGB color space specifies the green component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.
- `blue`: On return, the blue component of the color object. On applications linked for iOS 10 or later, an extended range sRGB color space specifies the blue component and can have any value. Values between `0.0` and `1.0` are inside the sRGB color gamut. On earlier versions of iOS, the specified value is always between `0.0` and `1.0`.
- `alpha`: On return, the opacity component of the color object, specified as a value between `0.0` and `1.0`.

## See Also

### Getting the color information
- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md)
  Change the system’s interpretation of a color value for display by selecting a color space.
- [var cgColor: CGColor](./cgcolor.md)
  The Quartz color that corresponds to the color object.
- [var ciColor: CIColor](./cicolor.md)
  The Core Image color that corresponds to the color object.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the components that form the color in the HSB color space.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./getwhite%28_,alpha%29.md)
  Returns the grayscale components of the color.
- [var linearExposure: CGFloat](./linearexposure.md)
  The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [var accessibilityName: String](./accessibilityname.md)
  A localized description of the color for accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/getred(_:green:blue:alpha:))*