# noteFocusRingMaskChanged()

**Framework**: AppKit  
**Kind**: method

Invoked to notify the view that the focus ring mask requires updating.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func noteFocusRingMaskChanged()
```

#### Discussion

It is important to note that it is only necessary for developers to invoke this method when some internal state change of their application, that AppKit can’t determine, affects the shape of the focus ring mask.

It is assumed that if the view is marked as needing display, or is resized, its focus ring shape is likely to have changed, and there is no need for clients to explicitly send this message in such cases, they are handled automatically.

If, however, a view is showing a focus ring around some part of its content (an `NSImage`, perhaps), and that content changes, the client must provide notification by invoking this method so that [`focusRingMaskBounds`](nsview/focusringmaskbounds.md) and [`drawFocusRingMask()`](nsview/drawfocusringmask().md) will be invoked to redraw the focus ring.

## See Also

- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](nsview/focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](nsview/drawfocusringmask.md)
  Draws the focus ring mask for the view.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](nsview/setkeyboardfocusringneedsdisplay(_:).md)
  Invalidates the area around the focus ring.
- [class var defaultFocusRingType: NSFocusRingType](nsview/defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/notefocusringmaskchanged())*