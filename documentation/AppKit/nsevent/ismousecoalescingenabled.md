# isMouseCoalescingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the system coalesces mouse movement events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var isMouseCoalescingEnabled: Bool { get set }
```

```objc
@property (class, getter=isMouseCoalescingEnabled) BOOL mouseCoalescingEnabled;
```

## Discussion

Mouse movement events include mouse-moved, mouse-dragged, and tablet events. If this property is [`true`](../../Swift/true.md), coalescing is enabled; otherwise, it’s disabled. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Getting gesture and touch information
- [var phase: NSEvent.Phase](./phase-swift.property.md)
  The phase of a gesture event, such as a magnify, scroll, or pressure change.
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [var magnification: CGFloat](./magnification.md)
  The amount of change to add to a magnification gesture.
- [func touches(matching: NSTouch.Phase, in: NSView?) -> Set<NSTouch>](./touches%28matching,in%29.md)
  Returns the touch objects associated with the specified phase.
- [func allTouches() -> Set<NSTouch>](./alltouches%28%29.md)
  Returns all touch objects associated with the event.
- [func touches(for: NSView) -> Set<NSTouch>](./touches%28for%29.md)
  Returns the touch objects from the event that belong to the specified view.
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](./coalescedtouches%28for%29.md)
  Returns all of the touch objects associated with the specified main touch.
- [NSEvent.GestureAxis](./gestureaxis.md)
  Constants that specify the direction of travel for a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/ismousecoalescingenabled)*