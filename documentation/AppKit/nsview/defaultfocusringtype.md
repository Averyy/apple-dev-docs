# defaultFocusRingType

**Framework**: AppKit  
**Kind**: property

Returns the default focus ring type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var defaultFocusRingType: NSFocusRingType { get }
```

#### Return Value

The default type of focus ring for objects of the view’s class. Possible return values are listed in [`NSFocusRingType`](nsfocusringtype.md).

#### Discussion

If the value in the [`focusRingType`](nsview/focusringtype.md) property is [`NSFocusRingType.default`](nsfocusringtype/default.md), the view can call this class method to find out what type of focus ring is the default. The view is free to ignore the default setting.

## See Also

- [var focusRingType: NSFocusRingType](nsview/focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](nsview/focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](nsview/drawfocusringmask.md)
  Draws the focus ring mask for the view.
- [func noteFocusRingMaskChanged()](nsview/notefocusringmaskchanged.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](nsview/setkeyboardfocusringneedsdisplay(_:).md)
  Invalidates the area around the focus ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/defaultfocusringtype)*