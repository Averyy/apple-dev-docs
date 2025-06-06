# NSEvent.EventType.smartMagnify

**Framework**: AppKit  
**Kind**: case

The user performed a smart-zoom gesture.

**Availability**:
- macOS 10.8+

## Declaration

```swift
case smartMagnify
```

#### Discussion

[`NSEvent.EventType.smartMagnify`](nsevent/eventtype/smartmagnify.md) represents the smart zoom gesture (that is, a two-finger double tap on trackpads), along with a corresponding [`NSResponder`](nsresponder.md) method. In response to this event, you should magnify the content appropriately for your app. For example, you might zoom in on a specific paragraph or image.

## See Also

- [NSEvent.EventType.beginGesture](nsevent/eventtype/begingesture.md)
  An event marking the beginning of a gesture.
- [NSEvent.EventType.endGesture](nsevent/eventtype/endgesture.md)
  An event that marks the end of a gesture.
- [NSEvent.EventType.magnify](nsevent/eventtype/magnify.md)
  The user performed a pinch-open or pinch-close gesture.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/smartmagnify)*