# colorSpace

**Framework**: AppKit  
**Kind**: property

The color space associated with the color.

**Availability**:
- macOS ?+

## Declaration

```swift
var colorSpace: NSColorSpace { get }
```

#### Discussion

Access this property only for colors that have an associated color space—specifically, colors not created by name or using a pattern image. Accessing it for other color types raises an exception. If you are unsure about a color object, convert it to an equivalent [`NSColorSpace`](nscolorspace.md)-based object before calling this method.

It is safe to access this property for color objects created with the color space names [`calibratedWhite`](nscolorspacename/calibratedwhite.md), [`NSCalibratedBlackColorSpace`](nscalibratedblackcolorspace.md), [`calibratedRGB`](nscolorspacename/calibratedrgb.md), [`deviceWhite`](nscolorspacename/devicewhite.md), [`NSDeviceBlackColorSpace`](nsdeviceblackcolorspace.md), [`deviceRGB`](nscolorspacename/devicergb.md), [`deviceCMYK`](nscolorspacename/devicecmyk.md), or [`custom`](nscolorspacename/custom.md)—or with the [`NSColorSpace`](nscolorspace.md) class methods corresponding to these names.

## See Also

- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [var type: NSColor.ColorType](nscolor/type.md)
  The type of the color object.
- [func usingType(NSColor.ColorType) -> NSColor?](nscolor/usingtype(_:).md)
  Returns a version of the color object that is compatible with the specified color type.
- [NSColor.ColorType](nscolor/colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [struct NSColorSpaceName](nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colorspace)*