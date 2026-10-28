# highlight(withLevel:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object that represents a blend between the current color and the highlight color.

**Availability**:
- macOS

## Declaration

```swift
func highlight(withLevel val: CGFloat) -> NSColor?
```

```objc
- (NSColor *) highlightWithLevel:(CGFloat) val;
```

## Return Value

The new `NSColor` object. Returns `nil` if the colors can’t be converted.

## Discussion

The highlight color is provided by the [`highlightColor`](./highlightcolor.md) property. Call this method when you want to brighten the current color for use in highlights.

## Parameters

- `val`: The amount of the highlight color that is blended with the receiver’s color. This should be a number from `0.0` through `1.0`. A `highlightLevel` below `0.0` is interpreted as `0.0`; a `highlightLevel` above `1.0` is interpreted as `1.0`.

## See Also

### Transforming existing color objects
- [func usingColorSpace(NSColorSpace) -> NSColor?](./usingcolorspace%28_%29.md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](./blended%28withfraction,of%29.md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](./withalphacomponent%28_%29.md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func shadow(withLevel: CGFloat) -> NSColor?](./shadow%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the shadow color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/highlight(withlevel:))*