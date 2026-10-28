# noteFocusRingMaskChanged()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to notify the view that the focus ring mask requires updating.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func noteFocusRingMaskChanged()
```

```objc
- (void) noteFocusRingMaskChanged;
```

## Discussion

It is important to note that it is only necessary for developers to invoke this method when some internal state change of their application, that AppKit can’t determine, affects the shape of the focus ring mask.

It is assumed that if the view is marked as needing display, or is resized, its focus ring shape is likely to have changed, and there is no need for clients to explicitly send this message in such cases, they are handled automatically.

If, however, a view is showing a focus ring around some part of its content (an `NSImage`, perhaps), and that content changes, the client must provide notification by invoking this method so that [`focusRingMaskBounds`](./focusringmaskbounds.md) and [`drawFocusRingMask()`](./drawfocusringmask%28%29.md) will be invoked to redraw the focus ring.

## See Also

### Drawing the Focus Ring
- [var focusRingType: NSFocusRingType](./focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](./focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](./drawfocusringmask%28%29.md)
  Draws the focus ring mask for the view.
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](./setkeyboardfocusringneedsdisplay%28_%29.md)
  Invalidates the area around the focus ring.
- [class var defaultFocusRingType: NSFocusRingType](./defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/notefocusringmaskchanged())*