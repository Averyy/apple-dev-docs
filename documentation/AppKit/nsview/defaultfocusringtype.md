# defaultFocusRingType

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default focus ring type.

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

The default type of focus ring for objects of the view’s class. Possible return values are listed in [`NSFocusRingType`](../nsfocusringtype.md).

## Discussion

If the value in the [`focusRingType`](./focusringtype.md) property is [`NSFocusRingType.default`](../nsfocusringtype/default.md), the view can call this class method to find out what type of focus ring is the default. The view is free to ignore the default setting.

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
- [func setKeyboardFocusRingNeedsDisplay(NSRect)](./setkeyboardfocusringneedsdisplay%28_%29.md)
  Invalidates the area around the focus ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/defaultfocusringtype)*