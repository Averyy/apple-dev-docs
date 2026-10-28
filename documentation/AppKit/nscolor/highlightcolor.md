# highlightColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use as a virtual light source on the screen.

**Availability**:
- macOS

## Declaration

```swift
class var highlightColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * highlightColor;
```

## Return Value

The system color for the virtual light source on the screen.

## Discussion

This method is invoked by the [`highlight(withLevel:)`](./highlight%28withlevel%29.md) method. For more information, see [`NSColor`](../nscolor.md).

## See Also

### Related Documentation
- [func highlight(withLevel: CGFloat) -> NSColor?](./highlight%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the highlight color.
### Highlights and shadows
- [class var findHighlightColor: NSColor](./findhighlightcolor.md)
  The highlight color to use for the bubble that shows inline search result values.
- [class var shadowColor: NSColor](./shadowcolor.md)
  The color to use for virtual shadows cast by raised objects on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor)*