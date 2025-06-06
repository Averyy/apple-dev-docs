# maskHelp

**Framework**: Core Graphics  
**Kind**: property

Indicates that the Help modifier key is down for a keyboard, mouse, or flag-changed event. This key is not present on most keyboards, and is different than the Help key found in the same row as Home and Page Up.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var maskHelp: CGEventFlags { get }
```

## See Also

- [static var maskAlphaShift: CGEventFlags](cgeventflags/maskalphashift.md)
  Indicates that the Caps Lock key is down for a keyboard, mouse, or flag-changed event.
- [static var maskShift: CGEventFlags](cgeventflags/maskshift.md)
  Indicates that the Shift key is down for a keyboard, mouse, or flag-changed event.
- [static var maskControl: CGEventFlags](cgeventflags/maskcontrol.md)
  Indicates that the Control key is down for a keyboard, mouse, or flag-changed event.
- [static var maskAlternate: CGEventFlags](cgeventflags/maskalternate.md)
  Indicates that the Alt or Option key is down for a keyboard, mouse, or flag-changed event.
- [static var maskCommand: CGEventFlags](cgeventflags/maskcommand.md)
  Indicates that the Command key is down for a keyboard, mouse, or flag-changed event.
- [static var maskSecondaryFn: CGEventFlags](cgeventflags/masksecondaryfn.md)
  Indicates that the Fn (Function) key is down for a keyboard, mouse, or flag-changed event. This key is found primarily on laptop keyboards.
- [static var maskNumericPad: CGEventFlags](cgeventflags/masknumericpad.md)
  Identifies key events from the numeric keypad area on extended keyboards.
- [static var maskNonCoalesced: CGEventFlags](cgeventflags/masknoncoalesced.md)
  Indicates that mouse and pen movement events are not being coalesced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventflags/maskhelp)*