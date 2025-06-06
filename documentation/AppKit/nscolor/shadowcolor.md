# shadowColor

**Framework**: AppKit  
**Kind**: property

The color to use for virtual shadows cast by raised objects on the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
class var shadowColor: NSColor { get }
```

#### Return Value

The system color for the virtual shadows case by raised objects on the screen.

#### Discussion

This method is invoked by [`shadow(withLevel:)`](nscolor/shadow(withlevel:).md). For general information about system colors, see [`Accessing System Colors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html#//apple_ref/doc/uid/20000790).

## See Also

- [func shadow(withLevel: CGFloat) -> NSColor?](nscolor/shadow(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the shadow color.
- [class var findHighlightColor: NSColor](nscolor/findhighlightcolor.md)
  The highlight color to use for the bubble that shows inline search result values.
- [class var highlightColor: NSColor](nscolor/highlightcolor.md)
  The color to use as a virtual light source on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor)*