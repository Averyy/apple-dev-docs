# NSEvent.EventType.tabletPoint

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The user touched a point on a tablet.

**Availability**:
- macOS

## Declaration

```swift
case tabletPoint
```

```c
NSEventTypeTabletPoint
```

## Discussion

Tablets generate tablet-point events between a mouse-down event and the first mouse drag event.

## See Also

### Getting Touch-Based Events
- [NSEvent.EventType.magnify](./magnify.md)
  The user performed a pinch-open or pinch-close gesture.
- [NSEvent.EventType.smartMagnify](./smartmagnify.md)
  The user performed a smart-zoom gesture.
- [NSEvent.EventType.swipe](./swipe.md)
  The user performed a swipe gesture.
- [NSEvent.EventType.rotate](./rotate.md)
  The user performed a rotate gesture.
- [NSEvent.EventType.gesture](./gesture.md)
  The user performed a nonspecific type of gesture.
- [NSEvent.EventType.directTouch](./directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletProximity](./tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](./pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/tabletpoint)*