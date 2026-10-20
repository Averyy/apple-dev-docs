# shadowColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use for virtual shadows cast by raised objects on the screen.

**Availability**:
- macOS

## Declaration

```swift
class var shadowColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * shadowColor;
```

#### Return Value

The system color for the virtual shadows case by raised objects on the screen.

#### Discussion

This method is invoked by [`shadow(withLevel:)`](./shadow%28withlevel%29.md). For more information, see [`NSColor`](../nscolor.md).

## See Also

### Related Documentation
- [func shadow(withLevel: CGFloat) -> NSColor?](./shadow%28withlevel%29.md)
  Creates a new color object that represents a blend between the current color and the shadow color.
### Highlights and shadows
- [class var findHighlightColor: NSColor](./findhighlightcolor.md)
  The highlight color to use for the bubble that shows inline search result values.
- [class var highlightColor: NSColor](./highlightcolor.md)
  The color to use as a virtual light source on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor)*