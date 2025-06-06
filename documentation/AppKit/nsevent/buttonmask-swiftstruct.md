# NSEvent.ButtonMask

**Framework**: AppKit  
**Kind**: struct

Constants you use to identify the activated tablet buttons in an event.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ButtonMask
```

## Topics

### Getting the Tablet Button Masks
- [static var penTip: NSEvent.ButtonMask](nsevent/buttonmask-swift.struct/pentip.md)
  A mask that matches the pen tip.
- [static var penLowerSide: NSEvent.ButtonMask](nsevent/buttonmask-swift.struct/penlowerside.md)
  A mask that matches the button on the lower side of the device.
- [static var penUpperSide: NSEvent.ButtonMask](nsevent/buttonmask-swift.struct/penupperside.md)
  A mask that matches the button on the upper side of the device.
### Initializers
- [init(rawValue: UInt)](nsevent/buttonmask-swift.struct/init(rawvalue:).md)

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
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/buttonmask-swift.struct)*