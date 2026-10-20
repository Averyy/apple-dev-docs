# NSEvent.GestureAxis

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the direction of travel for a gesture.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum GestureAxis
```

```c
enum NSEventGestureAxis : NSInteger;
```

## Topics

### Getting the Axis
- [NSEvent.GestureAxis.none](./gestureaxis/none.md)
  No specific axis.
- [NSEvent.GestureAxis.horizontal](./gestureaxis/horizontal.md)
  The horizontal axis.
- [NSEvent.GestureAxis.vertical](./gestureaxis/vertical.md)
  The vertical axis.
### Initializers
- [init?(rawValue: Int)](./gestureaxis/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [class var isMouseCoalescingEnabled: Bool](./ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/gestureaxis)*