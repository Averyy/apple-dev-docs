# ciColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The Core Image color that corresponds to the color object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var ciColor: CIColor { get }
```

```objc
@property (nonatomic, readonly) CIColor * CIColor;
```

#### Discussion

This property throws an exception if the color object wasn’t initialized with a Core Image color.

The color object in this property doesn’t adapt automatically to Dark Mode changes. If you use it to set the color of interface elements, you must update that color yourself. You update that color when the [`userInterfaceStyle`](../uitraitcollection/userinterfacestyle.md) trait of the current trait collection changes.

For information on how to apply color information reliably, see [Supporting Dark Mode in your interface](../supporting-dark-mode-in-your-interface.md).

## See Also

### Getting the color information
- [Determining color values with color spaces](../determining-color-values-with-color-spaces.md)
  Change the system’s interpretation of a color value for display by selecting a color space.
- [var cgColor: CGColor](./cgcolor.md)
  The Quartz color that corresponds to the color object.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the components that form the color in the HSB color space.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./getred%28_,green,blue,alpha%29.md)
  Returns the components that form the color in the RGB color space.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./getwhite%28_,alpha%29.md)
  Returns the grayscale components of the color.
- [var linearExposure: CGFloat](./linearexposure.md)
  The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [var accessibilityName: String](./accessibilityname.md)
  A localized description of the color for accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/cicolor)*