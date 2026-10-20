# maskAlphaShift

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

Indicates that the Caps Lock key is down for a keyboard, mouse, or flag-changed event.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var maskAlphaShift: CGEventFlags { get }
```

```c
kCGEventFlagMaskAlphaShift
```

## See Also

### Constants
- [static var maskShift: CGEventFlags](./maskshift.md)
  Indicates that the Shift key is down for a keyboard, mouse, or flag-changed event.
- [static var maskControl: CGEventFlags](./maskcontrol.md)
  Indicates that the Control key is down for a keyboard, mouse, or flag-changed event.
- [static var maskAlternate: CGEventFlags](./maskalternate.md)
  Indicates that the Alt or Option key is down for a keyboard, mouse, or flag-changed event.
- [static var maskCommand: CGEventFlags](./maskcommand.md)
  Indicates that the Command key is down for a keyboard, mouse, or flag-changed event.
- [static var maskHelp: CGEventFlags](./maskhelp.md)
  Indicates that the Help modifier key is down for a keyboard, mouse, or flag-changed event. This key is not present on most keyboards, and is different than the Help key found in the same row as Home and Page Up.
- [static var maskSecondaryFn: CGEventFlags](./masksecondaryfn.md)
  Indicates that the Fn (Function) key is down for a keyboard, mouse, or flag-changed event. This key is found primarily on laptop keyboards.
- [static var maskNumericPad: CGEventFlags](./masknumericpad.md)
  Identifies key events from the numeric keypad area on extended keyboards.
- [static var maskNonCoalesced: CGEventFlags](./masknoncoalesced.md)
  Indicates that mouse and pen movement events are not being coalesced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventflags/maskalphashift)*