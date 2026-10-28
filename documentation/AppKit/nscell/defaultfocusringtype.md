# defaultFocusRingType

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default type of focus ring for the receiver.

**Availability**:
- macOS

## Declaration

```swift
class var defaultFocusRingType: NSFocusRingType { get }
```

```objc
@property (class, readonly) NSFocusRingType defaultFocusRingType;
```

## Return Value

The default type of focus ring for the receiver (one of the values listed in [`NSFocusRingType`](../nsfocusringtype.md)).

## See Also

### Managing Focus Rings
- [func drawFocusRingMask(withFrame: NSRect, in: NSView)](./drawfocusringmask%28withframe,in%29.md)
  Draws the focus ring for the control.
- [func focusRingMaskBounds(forFrame: NSRect, in: NSView) -> NSRect](./focusringmaskbounds%28forframe,in%29.md)
  Returns the bounds of the focus ring mask.
- [var focusRingType: NSFocusRingType](./focusringtype.md)
  The type of focus ring to use with the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/defaultfocusringtype)*