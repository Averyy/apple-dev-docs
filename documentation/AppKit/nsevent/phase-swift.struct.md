# NSEvent.Phase

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that represent the possible phases during an event phase.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct Phase
```

```c
enum NSEventPhase : NSUInteger;
```

## Topics

### Constants
- [static var began: NSEvent.Phase](./phase-swift.struct/began.md)
  An event phase has begun.
- [static var stationary: NSEvent.Phase](./phase-swift.struct/stationary.md)
  An event phase is in progress but hasn’t moved since the previous event.
- [static var changed: NSEvent.Phase](./phase-swift.struct/changed.md)
  An event phase has changed.
- [static var ended: NSEvent.Phase](./phase-swift.struct/ended.md)
  The event phase ended.
- [static var cancelled: NSEvent.Phase](./phase-swift.struct/cancelled.md)
  The system canceled the event phase.
- [static var mayBegin: NSEvent.Phase](./phase-swift.struct/maybegin.md)
  The system event phase may begin.
### Initializers
- [init(rawValue: UInt)](./phase-swift.struct/init%28rawvalue%29.md)

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
- [NSEvent.SwipeTrackingOptions](./swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/phase-swift.struct)*