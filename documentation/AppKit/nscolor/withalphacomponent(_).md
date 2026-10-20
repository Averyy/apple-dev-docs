# withAlphaComponent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.

**Availability**:
- macOS

## Declaration

```swift
func withAlphaComponent(_ alpha: CGFloat) -> NSColor
```

```objc
- (NSColor *) colorWithAlphaComponent:(CGFloat) alpha;
```

#### Return Value

The new `NSColor` object. If the receiver’s color space doesn’t include an alpha component, the receiver is returned.

#### Discussion

A subclass with explicit opacity components should override this method to return a color with the specified alpha.

## Parameters

- `alpha`: The opacity value of the new `NSColor` object.

## See Also

### Related Documentation
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
### Transforming existing color objects
- [func usingColorSpace(NSColorSpace) -> NSColor?](./usingcolorspace%28_%29.md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](./blended%28withfraction,of%29.md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func highlight(withLevel: CGFloat) -> NSColor?](./highlight%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](./shadow%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the shadow color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/withalphacomponent(_:))*