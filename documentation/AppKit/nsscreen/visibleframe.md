# visibleFrame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current location and dimensions of the visible screen.

**Availability**:
- macOS

## Declaration

```swift
var visibleFrame: NSRect { get }
```

```objc
@property (readonly) NSRect visibleFrame;
```

## Discussion

This rectangle defines the portion of the screen in which it is currently safe to draw your app’s content.

The returned rectangle is always based on the current user-interface settings and does not include the area currently occupied by the dock and menu bar. On Macs that include a camera housing in the bezel, this rectangle does not include the bezel or the visible areas on either side of the bezel. Get those areas using the [`auxiliaryTopLeftArea`](./auxiliarytopleftarea-uglc.md) and [`auxiliaryTopRightArea`](./auxiliarytoprightarea-gr2n.md) properties. Don’t cache the rectangle in this property; it is based on the current user-interface settings, which can change between calls.

> **Note**:  Even when dock hiding is enabled, the rectangle returned by this method may be smaller than the full screen. The system uses a small boundary area to determine when it displays the dock.

## See Also

### Related Documentation
- [var frame: NSRect](./frame.md)
  The dimensions and location of the screen.
### Getting the Visible Portion of the Screen
- [var safeAreaInsets: NSEdgeInsets](./safeareainsets.md)
  The distances from the screen’s edges at which content isn’t obscured.
- [var auxiliaryTopLeftArea: NSRect?](./auxiliarytopleftarea-uglc.md)
  The unobscured portion of the top-left corner of the screen.
- [var auxiliaryTopRightArea: NSRect?](./auxiliarytoprightarea-gr2n.md)
  The unobscured portion of the top-right corner of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/visibleframe)*