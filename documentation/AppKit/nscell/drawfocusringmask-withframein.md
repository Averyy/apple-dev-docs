# drawFocusRingMask(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the focus ring for the control.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawFocusRingMask(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

Implemented by NSCell subclasses to draw the appropriate focus ring for the control The default implementation does nothing.

The Application Kit automatically invokes this method when appropriate, to render the view’s focus ring. The view must be eligible to become its window’s [`firstResponder`](nswindow/firstresponder.md), by overriding [`acceptsFirstResponder`](nsresponder/acceptsfirstresponder.md) returning [`true`](https://developer.apple.com/documentation/swift/true).

The focus ring is rendered using the style specified by the [`focusRingType`](nscell/focusringtype.md) property, which must not be [`NSFocusRingType.none`](nsfocusringtype/none.md) unless you want to suppress drawing of the focus ring. An implementation of `drawFocusRingMaskWithFrame:inView:` can assume that it is drawing in the view’s bounds, and that the fill and stroke colors have been set to an arbitrary fully opaque color. It needs only draw the desired focus ring shape or an image or other object whose outline defines the focus ring mask.

This new OS X v10.7 focus ring API should no longer call [`set()`](nsfocusringplacement/set().md)() and perform it’s own drawing.

## Parameters

- `cellFrame`: The bounding rectangle of the receiver, or a portion of the bounding rectangle.
- `controlView`: The view that manages the cell.

## See Also

- [func focusRingMaskBounds(forFrame: NSRect, in: NSView) -> NSRect](nscell/focusringmaskbounds(forframe:in:).md)
  Returns the bounds of the focus ring mask.
- [class var defaultFocusRingType: NSFocusRingType](nscell/defaultfocusringtype.md)
  Returns the default type of focus ring for the receiver.
- [var focusRingType: NSFocusRingType](nscell/focusringtype.md)
  The type of focus ring to use with the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/drawfocusringmask(withframe:in:))*