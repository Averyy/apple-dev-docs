# smartMagnify

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A mask for smart-zoom gesture events.

**Availability**:
- macOS 10.8+

## Declaration

```swift
static var smartMagnify: NSEvent.EventTypeMask { get }
```

```c
NSEventMaskSmartMagnify
```

#### Discussion

In response to this event, magnify the content appropriately for your app. For example, you might zoom in on a specific paragraph or image.

## See Also

### Getting Touch Events
- [static var magnify: NSEvent.EventTypeMask](./magnify.md)
  A mask for magnify-gesture events.
- [static var swipe: NSEvent.EventTypeMask](./swipe.md)
  A mask for swipe-gesture events.
- [static var rotate: NSEvent.EventTypeMask](./rotate.md)
  A mask for rotate-gesture events.
- [static var gesture: NSEvent.EventTypeMask](./gesture.md)
  A mask for generic gesture events.
- [static var directTouch: NSEvent.EventTypeMask](./directtouch.md)
  A mask for touch events.
- [static var tabletPoint: NSEvent.EventTypeMask](./tabletpoint.md)
  A mask for tablet-point events.
- [static var tabletProximity: NSEvent.EventTypeMask](./tabletproximity.md)
  A mask for tablet-proximity events.
- [static var pressure: NSEvent.EventTypeMask](./pressure.md)
  A mask for pressure-change events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/smartmagnify)*