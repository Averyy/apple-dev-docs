# usingColorSpaceName(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func usingColorSpaceName(_ name: NSColorSpaceName) -> NSColor?
```

#### Return Value

The new `NSColor` object or `nil` if the specified conversion cannot be done.

## Parameters

- `name`: The name of the color space containing the new   object.

## See Also

- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [func usingColorSpace(NSColorSpace) -> NSColor?](nscolor/usingcolorspace(_:).md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](nscolor/blended(withfraction:of:).md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](nscolor/withalphacomponent(_:).md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](nscolor/shadow(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the shadow color.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspacename(_:))*