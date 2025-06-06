# ended

**Framework**: AppKit  
**Kind**: property

A finger was lifted from the screen. Or, an active touch transitioned to a resting touch and resting touches are not wanted by the view hierarchy.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var ended: NSTouch.Phase { get }
```

## See Also

- [static var began: NSTouch.Phase](nstouch/phase-swift.struct/began.md)
  A finger touched the device. Or, a resting touch transitioned to an active touch and resting touches are not wanted by the view hierarchy.
- [static var moved: NSTouch.Phase](nstouch/phase-swift.struct/moved.md)
  A finger moved on the device.
- [static var stationary: NSTouch.Phase](nstouch/phase-swift.struct/stationary.md)
  A finger is touching the device, but hasn’t moved since the previous event.
- [static var cancelled: NSTouch.Phase](nstouch/phase-swift.struct/cancelled.md)
  The system cancelled tracking for the touch, as when (for example) the window associated with the touch resigns key or is deactivated.
- [static var touching: NSTouch.Phase](nstouch/phase-swift.struct/touching.md)
  Matches the [`began`](nstouch/phase-swift.struct/began.md), [`moved`](nstouch/phase-swift.struct/moved.md), or [`stationary`](nstouch/phase-swift.struct/stationary.md) phases of a touch.
- [static var any: NSTouch.Phase](nstouch/phase-swift.struct/any.md)
  Matches any phase of a touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/phase-swift.struct/ended)*