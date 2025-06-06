# shadow(withLevel:)

**Framework**: AppKit  
**Kind**: method

Creates a new color object that represents a blend between the current color and the shadow color.

**Availability**:
- macOS ?+

## Declaration

```swift
func shadow(withLevel val: CGFloat) -> NSColor?
```

#### Return Value

The new `NSColor` object. Returns `nil` if the colors can’t be converted.

#### Discussion

The shadow color is provided by the [`shadowColor`](nscolor/shadowcolor.md) property. Call this method when you want to darken the current color for use in shadows.

## Parameters

- `val`: The amount of the shadow color used for the blend. This should be a number from   through  .  A   below   is interpreted as  ; a   above   is interpreted as  .

## See Also

- [func usingColorSpace(NSColorSpace) -> NSColor?](nscolor/usingcolorspace(_:).md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](nscolor/blended(withfraction:of:).md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](nscolor/withalphacomponent(_:).md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/shadow(withlevel:))*