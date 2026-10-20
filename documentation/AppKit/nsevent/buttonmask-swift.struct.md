# NSEvent.ButtonMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants you use to identify the activated tablet buttons in an event.

**Availability**:
- macOS

## Declaration

```swift
struct ButtonMask
```

```c
enum NSEventButtonMask : NSUInteger;
```

## Topics

### Getting the Tablet Button Masks
- [static var penTip: NSEvent.ButtonMask](./buttonmask-swift.struct/pentip.md)
  A mask that matches the pen tip.
- [static var penLowerSide: NSEvent.ButtonMask](./buttonmask-swift.struct/penlowerside.md)
  A mask that matches the button on the lower side of the device.
- [static var penUpperSide: NSEvent.ButtonMask](./buttonmask-swift.struct/penupperside.md)
  A mask that matches the button on the upper side of the device.
### Initializers
- [init(rawValue: UInt)](./buttonmask-swift.struct/init%28rawvalue%29.md)

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
- [NSEvent.ModifierFlags](./modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](./swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/buttonmask-swift.struct)*