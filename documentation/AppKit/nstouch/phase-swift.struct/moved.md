# moved

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A finger moved on the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var moved: NSTouch.Phase { get }
```

```c
NSTouchPhaseMoved
```

## See Also

### Constants
- [static var began: NSTouch.Phase](./began.md)
  A finger touched the device. Or, a resting touch transitioned to an active touch and resting touches are not wanted by the view hierarchy.
- [static var stationary: NSTouch.Phase](./stationary.md)
  A finger is touching the device, but hasn’t moved since the previous event.
- [static var ended: NSTouch.Phase](./ended.md)
  A finger was lifted from the screen. Or, an active touch transitioned to a resting touch and resting touches are not wanted by the view hierarchy.
- [static var cancelled: NSTouch.Phase](./cancelled.md)
  The system cancelled tracking for the touch, as when (for example) the window associated with the touch resigns key or is deactivated.
- [static var touching: NSTouch.Phase](./touching.md)
  Matches the [`began`](./began.md), [`moved`](./moved.md), or [`stationary`](./stationary.md) phases of a touch.
- [static var any: NSTouch.Phase](./any.md)
  Matches any phase of a touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/phase-swift.struct/moved)*