# setKeyboardFocusRingNeedsDisplay(_:)

**Framework**: AppKit  
**Kind**: method

Invalidates the area around the focus ring.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setKeyboardFocusRingNeedsDisplay(_ rect: NSRect)
```

## Parameters

- `rect`: The rectangle of the control or cell defining the area around the focus ring.   will be expanded to include the focus ring for invalidation.

## See Also

- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](nsview/focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](nsview/drawfocusringmask.md)
  Draws the focus ring mask for the view.
- [func noteFocusRingMaskChanged()](nsview/notefocusringmaskchanged.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [class var defaultFocusRingType: NSFocusRingType](nsview/defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setkeyboardfocusringneedsdisplay(_:))*