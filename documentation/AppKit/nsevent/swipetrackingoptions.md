# NSEvent.SwipeTrackingOptions

**Framework**: AppKit  
**Kind**: struct

Constants that specify swipe-tracking options.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct SwipeTrackingOptions
```

## Topics

### Constants
- [static var lockDirection: NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions/lockdirection.md)
  Clamp gestureAmount to 0 if the user starts to swipe in the opposite direction than they started.
- [static var clampGestureAmount: NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions/clampgestureamount.md)
  Don’t allow gestureAmount to go beyond +/-1.0
### Initializers
- [init(rawValue: UInt)](nsevent/swipetrackingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/swipetrackingoptions)*