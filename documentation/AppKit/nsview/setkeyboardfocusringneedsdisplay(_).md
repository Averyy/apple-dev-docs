# setKeyboardFocusRingNeedsDisplay(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the area around the focus ring.

**Availability**:
- macOS

## Declaration

```swift
func setKeyboardFocusRingNeedsDisplay(_ rect: NSRect)
```

```objc
- (void) setKeyboardFocusRingNeedsDisplayInRect:(NSRect) rect;
```

## Parameters

- `rect`: The rectangle of the control or cell defining the area around the focus ring. `rect` will be expanded to include the focus ring for invalidation.

## See Also

### Drawing the Focus Ring
- [var focusRingType: NSFocusRingType](./focusringtype.md)
  The type of focus ring drawn around the view.
- [var focusRingMaskBounds: NSRect](./focusringmaskbounds.md)
  The focus ring mask bounds, specified in the view’s coordinate space.
- [func drawFocusRingMask()](./drawfocusringmask%28%29.md)
  Draws the focus ring mask for the view.
- [func noteFocusRingMaskChanged()](./notefocusringmaskchanged%28%29.md)
  Invoked to notify the view that the focus ring mask requires updating.
- [class var defaultFocusRingType: NSFocusRingType](./defaultfocusringtype.md)
  Returns the default focus ring type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setkeyboardfocusringneedsdisplay(_:))*