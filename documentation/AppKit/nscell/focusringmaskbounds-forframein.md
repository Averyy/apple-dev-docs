# focusRingMaskBounds(forFrame:in:)

**Framework**: AppKit  
**Kind**: method

Returns the bounds of the focus ring mask.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func focusRingMaskBounds(forFrame cellFrame: NSRect, in controlView: NSView) -> NSRect
```

#### Return Value

Returns a rectangle encompassing the focus ring bounds in the `controlView` coordinate space.

#### Discussion

Implemented by `NSCell` subclasses to allow the cell to provide the rectangular bounds of the focus ring mask for the cell.

The default implementation returns an empty value. Subclasses are expected to implement this method if they intend to draw a focus ring.

## Parameters

- `cellFrame`: The bounding rectangle of the receiver, or a portion of the bounding rectangle.
- `controlView`: The view that manages the cell.

## See Also

- [func drawFocusRingMask(withFrame: NSRect, in: NSView)](nscell/drawfocusringmask(withframe:in:).md)
  Draws the focus ring for the control.
- [class var defaultFocusRingType: NSFocusRingType](nscell/defaultfocusringtype.md)
  Returns the default type of focus ring for the receiver.
- [var focusRingType: NSFocusRingType](nscell/focusringtype.md)
  The type of focus ring to use with the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/focusringmaskbounds(forframe:in:))*