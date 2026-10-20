# NSEvent.SwipeTrackingOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify swipe-tracking options.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct SwipeTrackingOptions
```

```c
enum NSEventSwipeTrackingOptions : NSUInteger;
```

## Topics

### Constants
- [static var lockDirection: NSEvent.SwipeTrackingOptions](./swipetrackingoptions/lockdirection.md)
  Clamp gestureAmount to 0 if the user starts to swipe in the opposite direction than they started.
- [static var clampGestureAmount: NSEvent.SwipeTrackingOptions](./swipetrackingoptions/clampgestureamount.md)
  Don’t allow gestureAmount to go beyond +/-1.0
### Initializers
- [init(rawValue: UInt)](./swipetrackingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSEvent.EventTypeMask](./eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.ButtonMask](./buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.ModifierFlags](./modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/swipetrackingoptions)*