# NSEvent.ModifierFlags

**Framework**: AppKit  
**Kind**: struct

Flags that represent key states in an event object.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ModifierFlags
```

## Topics

### Event Modifier Flags
- [static var capsLock: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/capslock.md)
  The Caps Lock key has been pressed.
- [static var shift: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/shift.md)
  The Shift key has been pressed.
- [static var control: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/control.md)
  The Control key has been pressed.
- [static var option: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/option.md)
  The Option or Alt key has been pressed.
- [static var command: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/command.md)
  The Command key has been pressed.
- [static var numericPad: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/numericpad.md)
  A key in the numeric keypad or an arrow key has been pressed.
- [static var help: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/help.md)
  The Help key has been pressed.
- [static var function: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/function.md)
  A function key has been pressed.
- [static var deviceIndependentFlagsMask: NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct/deviceindependentflagsmask.md)
  Device-independent modifier flags are masked.
### Deprecated
- [init(rawValue: UInt)](nsevent/modifierflags-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.struct)*