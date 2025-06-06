# highlightColor

**Framework**: AppKit  
**Kind**: property

The color to use as a virtual light source on the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
class var highlightColor: NSColor { get }
```

#### Return Value

The system color for the virtual light source on the screen.

#### Discussion

This method is invoked by the [`highlight(withLevel:)`](nscolor/highlight(withlevel:).md) method. For general information about system colors, see [`Accessing System Colors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html#//apple_ref/doc/uid/20000790).

## See Also

- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [class var findHighlightColor: NSColor](nscolor/findhighlightcolor.md)
  The highlight color to use for the bubble that shows inline search result values.
- [class var shadowColor: NSColor](nscolor/shadowcolor.md)
  The color to use for virtual shadows cast by raised objects on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor)*