# usingColorSpace(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object representing the color of the current color object in the specified color space.

**Availability**:
- macOS

## Declaration

```swift
func usingColorSpace(_ space: NSColorSpace) -> NSColor?
```

```objc
- (NSColor *) colorUsingColorSpace:(NSColorSpace *) space;
```

## Return Value

The new `NSColor` object. This method converts the receiver’s color to an equivalent one in the new color space. Although the new color might have different component values, it looks the same as the original.  Returns `nil` if conversion is not possible.

## Discussion

If the receiver’s color space is the same as that specified in `space`, this method returns the same `NSColor` object.

## Parameters

- `space`: The color space of the new `NSColor` object.

## See Also

### Related Documentation
- [init(colorSpace: NSColorSpace, components: UnsafePointer<CGFloat>, count: Int)](./init%28colorspace,components,count%29.md)
  Creates a color object from the specified components of the given color space.
### Transforming existing color objects
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](./blended%28withfraction,of%29.md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](./withalphacomponent%28_%29.md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](./highlight%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](./shadow%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the shadow color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspace(_:))*