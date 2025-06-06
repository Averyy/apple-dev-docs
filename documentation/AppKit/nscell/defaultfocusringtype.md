# defaultFocusRingType

**Framework**: AppKit  
**Kind**: property

Returns the default type of focus ring for the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var defaultFocusRingType: NSFocusRingType { get }
```

#### Return Value

The default type of focus ring for the receiver (one of the values listed in [`NSFocusRingType`](nsfocusringtype.md)).

## See Also

- [func drawFocusRingMask(withFrame: NSRect, in: NSView)](nscell/drawfocusringmask(withframe:in:).md)
  Draws the focus ring for the control.
- [func focusRingMaskBounds(forFrame: NSRect, in: NSView) -> NSRect](nscell/focusringmaskbounds(forframe:in:).md)
  Returns the bounds of the focus ring mask.
- [var focusRingType: NSFocusRingType](nscell/focusringtype.md)
  The type of focus ring to use with the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/defaultfocusringtype)*