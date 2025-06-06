# visibleFrame

**Framework**: Appkit  
**Kind**: property

The current location and dimensions of the visible screen.

**Availability**:
- macOS ?+

## Declaration

```swift
var visibleFrame: NSRect { get }
```

#### Discussion

This rectangle defines the portion of the screen in which it is currently safe to draw your app’s content.

The returned rectangle is always based on the current user-interface settings and does not include the area currently occupied by the dock and menu bar. On Macs that include a camera housing in the bezel, this rectangle does not include the bezel or the visible areas on either side of the bezel. Get those areas using the [`auxiliaryTopLeftArea`](nsscreen/auxiliarytopleftarea-uglc.md) and [`auxiliaryTopRightArea`](nsscreen/auxiliarytoprightarea-gr2n.md) properties. Don’t cache the rectangle in this property; it is based on the current user-interface settings, which can change between calls.

> **Note**:  Even when dock hiding is enabled, the rectangle returned by this method may be smaller than the full screen. The system uses a small boundary area to determine when it displays the dock.

## See Also

- [var frame: NSRect](nsscreen/frame.md)
  The dimensions and location of the screen.
- [var safeAreaInsets: NSEdgeInsets](nsscreen/safeareainsets.md)
  The distances from the screen’s edges at which content isn’t obscured.
- [var auxiliaryTopLeftArea: NSRect?](nsscreen/auxiliarytopleftarea-uglc.md)
  The unobscured portion of the top-left corner of the screen.
- [var auxiliaryTopRightArea: NSRect?](nsscreen/auxiliarytoprightarea-gr2n.md)
  The unobscured portion of the top-right corner of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsscreen/visibleframe)*