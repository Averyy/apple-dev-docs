# NSEvent.EventType.gesture

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The user performed a nonspecific type of gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case gesture
```

```c
NSEventTypeGesture
```

## Discussion

[`NSEvent.EventType.gesture`](./gesture.md) represents a gesture that is not otherwise specified by a type such as [`NSEvent.EventType.magnify`](./magnify.md), [`NSEvent.EventType.swipe`](./swipe.md), [`NSEvent.EventType.rotate`](./rotate.md), [`NSEvent.EventType.beginGesture`](./begingesture.md), or [`NSEvent.EventType.endGesture`](./endgesture.md)

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
- [NSEvent.EventType.directTouch](./directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletPoint](./tabletpoint.md)
  The user touched a point on a tablet.
- [NSEvent.EventType.tabletProximity](./tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](./pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/gesture)*