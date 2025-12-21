# blended(withFraction:of:)

**Framework**: AppKit  
**Kind**: method

Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.

**Availability**:
- macOS ?+

## Declaration

```swift
func blended(withFraction fraction: CGFloat, of color: NSColor) -> NSColor?
```

#### Return Value

The resulting color object or `nil` if the colors can’t be converted.

## Parameters

- `fraction`: The amount of the color to blend with the receiver’s color. The method converts   and a copy of the receiver to RGB, and then sets each component of the returned color to   of  ‘s value plus 1 –   of the receiver’s.
- `color`: The color to blend with the receiver’s color.

## See Also

- [func usingColorSpace(NSColorSpace) -> NSColor?](nscolor/usingcolorspace(_:).md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func withAlphaComponent(CGFloat) -> NSColor](nscolor/withalphacomponent(_:).md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](nscolor/shadow(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the shadow color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/blended(withfraction:of:))*