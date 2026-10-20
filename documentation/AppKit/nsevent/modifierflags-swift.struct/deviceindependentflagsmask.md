# deviceIndependentFlagsMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Device-independent modifier flags are masked.

**Availability**:
- macOS

## Declaration

```swift
static var deviceIndependentFlagsMask: NSEvent.ModifierFlags { get }
```

```c
NSEventModifierFlagDeviceIndependentFlagsMask
```

#### Discussion

Use this symbol to preserve key event flags and mask all other flags.

## See Also

### Event Modifier Flags
- [static var capsLock: NSEvent.ModifierFlags](./capslock.md)
  The Caps Lock key has been pressed.
- [static var shift: NSEvent.ModifierFlags](./shift.md)
  The Shift key has been pressed.
- [static var control: NSEvent.ModifierFlags](./control.md)
  The Control key has been pressed.
- [static var option: NSEvent.ModifierFlags](./option.md)
  The Option or Alt key has been pressed.
- [static var command: NSEvent.ModifierFlags](./command.md)
  The Command key has been pressed.
- [static var numericPad: NSEvent.ModifierFlags](./numericpad.md)
  A key in the numeric keypad or an arrow key has been pressed.
- [static var help: NSEvent.ModifierFlags](./help.md)
  The Help key has been pressed.
- [static var function: NSEvent.ModifierFlags](./function.md)
  A function key has been pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.struct/deviceindependentflagsmask)*