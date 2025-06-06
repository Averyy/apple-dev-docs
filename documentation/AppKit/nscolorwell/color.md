# color

**Framework**: AppKit  
**Kind**: property

The currently selected color for the color well.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var color: NSColor { get set }
```

#### Discussion

Use this property to get the currently selected color, or to set the current color programmatically.

## See Also

- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)
- [func takeColorFrom(Any?)](nscolorwell/takecolorfrom(_:).md)
  Changes the currently selected color to the color of the specified object.
- [var supportsAlpha: Bool](nscolorwell/supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/color)*