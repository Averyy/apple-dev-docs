# backingScaleFactor

**Framework**: AppKit  
**Kind**: property

The backing store pixel scale factor for the screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var backingScaleFactor: CGFloat { get }
```

#### Discussion

This is the scale factor representing the number of backing store pixels corresponding to each linear unit in screen space on this screen.

This method is provided for rare cases when the explicit scale factor is needed.  As often as possible, you should use the [`NSView`](nsview.md) class’s convert backing methods.

## See Also

- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nsscreen/backingalignedrect(_:options:).md)
  Converts a rectangle in global screen coordinates to a pixel aligned rectangle.
- [func convertRectFromBacking(NSRect) -> NSRect](nsscreen/convertrectfrombacking(_:).md)
  Converts the rectangle from the device pixel aligned coordinates system of a screen.
- [func convertRectToBacking(NSRect) -> NSRect](nsscreen/convertrecttobacking(_:).md)
  Converts the rectangle to the device pixel aligned coordinates system of a screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/backingscalefactor)*