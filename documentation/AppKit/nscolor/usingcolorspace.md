# usingColorSpace(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new color object representing the color of the current color object in the specified color space.

**Availability**:
- macOS ?+

## Declaration

```swift
func usingColorSpace(_ space: NSColorSpace) -> NSColor?
```

#### Return Value

The new `NSColor` object. This method converts the receiver’s color to an equivalent one in the new color space. Although the new color might have different component values, it looks the same as the original.  Returns `nil` if conversion is not possible.

#### Discussion

If the receiver’s color space is the same as that specified in `space`, this method returns the same `NSColor` object.

## Parameters

- `space`: The color space of the new   object.

## See Also

- [init(colorSpace: NSColorSpace, components: UnsafePointer<CGFloat>, count: Int)](nscolor/init(colorspace:components:count:).md)
  Creates a color object from the specified components of the given color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](nscolor/blended(withfraction:of:).md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](nscolor/withalphacomponent(_:).md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](nscolor/shadow(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the shadow color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspace(_:))*