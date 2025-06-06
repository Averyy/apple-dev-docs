# NSEvent.Phase

**Framework**: AppKit  
**Kind**: struct

Constants that represent the possible phases during an event phase.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct Phase
```

## Topics

### Constants
- [static var began: NSEvent.Phase](nsevent/phase-swift.struct/began.md)
  An event phase has begun.
- [static var stationary: NSEvent.Phase](nsevent/phase-swift.struct/stationary.md)
  An event phase is in progress but hasn’t moved since the previous event.
- [static var changed: NSEvent.Phase](nsevent/phase-swift.struct/changed.md)
  An event phase has changed.
- [static var ended: NSEvent.Phase](nsevent/phase-swift.struct/ended.md)
  The event phase ended.
- [static var cancelled: NSEvent.Phase](nsevent/phase-swift.struct/cancelled.md)
  The system canceled the event phase.
- [static var mayBegin: NSEvent.Phase](nsevent/phase-swift.struct/maybegin.md)
  The system event phase may begin.
### Initializers
- [init(rawValue: UInt)](nsevent/phase-swift.struct/init(rawvalue:).md)

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
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/phase-swift.struct)*