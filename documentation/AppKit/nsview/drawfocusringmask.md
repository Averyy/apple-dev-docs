# drawFocusRingMask()

**Framework**: AppKit  
**Kind**: method

Draws the focus ring mask for the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawFocusRingMask()
```

#### Discussion

This method provides the shape of the focus ring mask by drawing the focus ring mask. An implementation of this method should draw in the view’s interior (bounds) coordinate space, that the focus ring style has been set (it will be set it to [`NSFocusRingPlacement.only`](nsfocusringplacement/only.md) to capture the focus ring itself), and that the fill and stroke colors have been set to an arbitrary fully opaque color.

Subclasses that find the default behavior insufficient should only draw the focus ring shape.

The `NSView` implementation of this method simply fills `[self bounds]`.

## See Also

- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](nsview/focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func noteFocusRingMaskChanged()](nsview/notefocusringmaskchanged.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](nsview/setkeyboardfocusringneedsdisplay(_:).md)
  Invalidates the area around the focus ring.
- [class var defaultFocusRingType: NSFocusRingType](nsview/defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/drawfocusringmask())*