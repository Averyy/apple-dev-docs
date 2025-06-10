# focusRingMaskBounds

**Framework**: AppKit  
**Kind**: property

The focus ring mask bounds, specified in the view’s coordinate space.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var focusRingMaskBounds: NSRect { get }
```

#### Discussion

The rectangle in this property is specified relative to the view’s interior (bounds) coordinate space. The mask bounds allows the focus ring’s overall size and position to be determined before it is drawn. Override this property if your view requires the display of a focus ring. The default value of this property is [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect).

> **Note**:  The information provided by this property enables Accessibility to identify selected subelements for zoom tracking, so it is important that this method provide a reasonably tight bounding box and that the [`noteFocusRingMaskChanged()`](nsview/notefocusringmaskchanged().md) method is called as described.

## See Also

- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [func drawFocusRingMask()](nsview/drawfocusringmask.md)
  Draws the focus ring mask for the view.
- [func noteFocusRingMaskChanged()](nsview/notefocusringmaskchanged.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](nsview/setkeyboardfocusringneedsdisplay(_:).md)
  Invalidates the area around the focus ring.
- [class var defaultFocusRingType: NSFocusRingType](nsview/defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/focusringmaskbounds)*