# NSEvent.ModifierFlags

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Flags that represent key states in an event object.

**Availability**:
- macOS

## Declaration

```swift
struct ModifierFlags
```

```c
enum NSEventModifierFlags : NSUInteger;
```

## Topics

### Event Modifier Flags
- [static var capsLock: NSEvent.ModifierFlags](./modifierflags-swift.struct/capslock.md)
  The Caps Lock key has been pressed.
- [static var shift: NSEvent.ModifierFlags](./modifierflags-swift.struct/shift.md)
  The Shift key has been pressed.
- [static var control: NSEvent.ModifierFlags](./modifierflags-swift.struct/control.md)
  The Control key has been pressed.
- [static var option: NSEvent.ModifierFlags](./modifierflags-swift.struct/option.md)
  The Option or Alt key has been pressed.
- [static var command: NSEvent.ModifierFlags](./modifierflags-swift.struct/command.md)
  The Command key has been pressed.
- [static var numericPad: NSEvent.ModifierFlags](./modifierflags-swift.struct/numericpad.md)
  A key in the numeric keypad or an arrow key has been pressed.
- [static var help: NSEvent.ModifierFlags](./modifierflags-swift.struct/help.md)
  The Help key has been pressed.
- [static var function: NSEvent.ModifierFlags](./modifierflags-swift.struct/function.md)
  A function key has been pressed.
- [static var deviceIndependentFlagsMask: NSEvent.ModifierFlags](./modifierflags-swift.struct/deviceindependentflagsmask.md)
  Device-independent modifier flags are masked.
### Deprecated
- [init(rawValue: UInt)](./modifierflags-swift.struct/init%28rawvalue%29.md)
- [Deprecated symbols](../modifierflags-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

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
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](./swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.struct)*