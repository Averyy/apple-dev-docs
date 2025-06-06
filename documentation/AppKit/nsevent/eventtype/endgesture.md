# NSEvent.EventType.endGesture

**Framework**: AppKit  
**Kind**: case

An event that marks the end of a gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case endGesture
```

#### Discussion

Note that apps that link against macOS 10.11 and later no longer receive this event type. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](nsevent/phase-swift.property.md) property instead.

## See Also

- [NSEvent.EventType.beginGesture](nsevent/eventtype/begingesture.md)
  An event marking the beginning of a gesture.
- [NSEvent.EventType.magnify](nsevent/eventtype/magnify.md)
  The user performed a pinch-open or pinch-close gesture.
- [NSEvent.EventType.smartMagnify](nsevent/eventtype/smartmagnify.md)
  The user performed a smart-zoom gesture.
- [NSEvent.EventType.swipe](nsevent/eventtype/swipe.md)
  The user performed a swipe gesture.
- [NSEvent.EventType.rotate](nsevent/eventtype/rotate.md)
  The user performed a rotate gesture.
- [NSEvent.EventType.gesture](nsevent/eventtype/gesture.md)
  The user performed a nonspecific type of gesture.
- [NSEvent.EventType.directTouch](nsevent/eventtype/directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletPoint](nsevent/eventtype/tabletpoint.md)
  The user touched a point on a tablet.
- [NSEvent.EventType.tabletProximity](nsevent/eventtype/tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](nsevent/eventtype/pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/endgesture)*