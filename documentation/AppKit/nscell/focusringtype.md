# focusRingType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of focus ring to use with the associated view.

**Availability**:
- macOS

## Declaration

```swift
var focusRingType: NSFocusRingType { get set }
```

```objc
@property NSFocusRingType focusRingType;
```

## Discussion

You can disable a view’s focus ring drawing by setting this property to [`NSFocusRingType.none`](../nsfocusringtype/none.md). The only times you should disable focus ring drawing are when you want to draw your own focus ring or when there is insufficient space to display a focus ring in the default location.

## See Also

### Managing Focus Rings
- [func drawFocusRingMask(withFrame: NSRect, in: NSView)](./drawfocusringmask%28withframe,in%29.md)
  Draws the focus ring for the control.
- [func focusRingMaskBounds(forFrame: NSRect, in: NSView) -> NSRect](./focusringmaskbounds%28forframe,in%29.md)
  Returns the bounds of the focus ring mask.
- [class var defaultFocusRingType: NSFocusRingType](./defaultfocusringtype.md)
  Returns the default type of focus ring for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/focusringtype)*