# NSEvent.EventType.smartMagnify

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The user performed a smart-zoom gesture.

**Availability**:
- macOS 10.8+

## Declaration

```swift
case smartMagnify
```

```c
NSEventTypeSmartMagnify
```

#### Discussion

[`NSEvent.EventType.smartMagnify`](./smartmagnify.md) represents the smart zoom gesture (that is, a two-finger double tap on trackpads), along with a corresponding [`NSResponder`](../../nsresponder.md) method. In response to this event, you should magnify the content appropriately for your app. For example, you might zoom in on a specific paragraph or image.

## See Also

### Getting Touch-Based Events
- [NSEvent.EventType.magnify](./magnify.md)
  The user performed a pinch-open or pinch-close gesture.
- [NSEvent.EventType.swipe](./swipe.md)
  The user performed a swipe gesture.
- [NSEvent.EventType.rotate](./rotate.md)
  The user performed a rotate gesture.
- [NSEvent.EventType.gesture](./gesture.md)
  The user performed a nonspecific type of gesture.
- [NSEvent.EventType.directTouch](./directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletPoint](./tabletpoint.md)
  The user touched a point on a tablet.
- [NSEvent.EventType.tabletProximity](./tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](./pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/smartmagnify)*