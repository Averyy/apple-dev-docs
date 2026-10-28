# NSDeviceIndependentModifierFlagsMask

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Device-independent modifier flags are masked.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```c
static const NSEventModifierFlags NSDeviceIndependentModifierFlagsMask;
```

## Discussion

Use this symbol to mask off device-dependent modifier flags, including event coalescing information. The result will contain only key event flags.

## See Also

### Deprecated constants
- [NSAlphaShiftKeyMask](./nsalphashiftkeymask.md)
  The Caps Lock key has been pressed.
- [NSShiftKeyMask](./nsshiftkeymask.md)
  The Shift key has been pressed.
- [NSControlKeyMask](./nscontrolkeymask.md)
  The Control key has been pressed.
- [NSAlternateKeyMask](./nsalternatekeymask.md)
  The Option or Alt key has been pressed.
- [NSCommandKeyMask](./nscommandkeymask.md)
  The Command key has been pressed.
- [NSNumericPadKeyMask](./nsnumericpadkeymask.md)
  A key in the numeric keypad or an arrow key has been pressed.
- [NSHelpKeyMask](./nshelpkeymask.md)
  The Help key has been pressed.
- [NSFunctionKeyMask](./nsfunctionkeymask.md)
  A function key has been pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdeviceindependentmodifierflagsmask)*