# set()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies how the system draws the focus ring.

**Availability**:
- macOS

## Declaration

```swift
func set()
```

```c
extern void NSSetFocusRingStyle(NSFocusRingPlacement placement);
```

#### Discussion

Use [`NSFocusRingPlacement.above`](./above.md) to draw the focus ring over an image, use [`NSFocusRingPlacement.below`](./below.md) to draw the focus ring under text, and use [`NSFocusRingPlacement.only`](./only.md) if you don’t have an image or text. For the [`NSFocusRingPlacement.only`](./only.md) case, fills a shape to add the focus ring around the shape.

Note that the focus ring may actually be drawn outside the view but will be clipped to any clipping superview or the window content view.

## See Also

### Drawing Focus Rings
- [enum NSFocusRingPlacement](../nsfocusringplacement.md)
  Constants that indicate how the system draws the focus ring.
- [enum NSFocusRingType](../nsfocusringtype.md)
  Constants that describe the style of the focus ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfocusringplacement/set())*