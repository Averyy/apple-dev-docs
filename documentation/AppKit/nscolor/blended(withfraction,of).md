# blended(withFraction:of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.

**Availability**:
- macOS

## Declaration

```swift
func blended(withFraction fraction: CGFloat, of color: NSColor) -> NSColor?
```

```objc
- (NSColor *) blendedColorWithFraction:(CGFloat) fraction ofColor:(NSColor *) color;
```

## Return Value

The resulting color object or `nil` if the colors can’t be converted.

## Parameters

- `fraction`: The amount of the color to blend with the receiver’s color. The method converts `color` and a copy of the receiver to RGB, and then sets each component of the returned color to `fraction` of `color`‘s value plus 1 – `fraction` of the receiver’s.
- `color`: The color to blend with the receiver’s color.

## See Also

### Transforming existing color objects
- [func usingColorSpace(NSColorSpace) -> NSColor?](./usingcolorspace%28_%29.md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func withAlphaComponent(CGFloat) -> NSColor](./withalphacomponent%28_%29.md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](./highlight%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](./shadow%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the shadow color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/blended(withfraction:of:))*