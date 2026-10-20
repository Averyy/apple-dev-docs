# NSEvent.SpecialKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for reserved function keys on the keyboard.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct SpecialKey
```

#### Overview

These constants correspond to unicode characters in the range (0xF700–0xF8FF) and are values you can use with the [`characters`](./characters.md) and [`charactersIgnoringModifiers`](./charactersignoringmodifiers.md) properties of the event. You can also use them in some parameters in the [`keyEvent(with:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:)`](./keyevent%28with,location,modifierflags,timestamp,windownumber,context,characters,charactersignoringmodifiers,isarepeat,keycode%29.md) method of the event.

Note that the system handles some function keys at a lower level and your app never sees them. Examples include the Volume Up key, Volume Down key, Volume Mute key, Eject key, and Function key found on many Macs.

## Topics

### Getting Common Control Keys
- [static let backspace: NSEvent.SpecialKey](./specialkey-swift.struct/backspace.md)
  The backspace key.
- [static let carriageReturn: NSEvent.SpecialKey](./specialkey-swift.struct/carriagereturn.md)
  The carriage return key.
- [static let newline: NSEvent.SpecialKey](./specialkey-swift.struct/newline.md)
  The newline key.
- [static let enter: NSEvent.SpecialKey](./specialkey-swift.struct/enter.md)
  The enter key.
- [static let delete: NSEvent.SpecialKey](./specialkey-swift.struct/delete.md)
  The delete key.
- [static let deleteForward: NSEvent.SpecialKey](./specialkey-swift.struct/deleteforward.md)
  The delete forward key.
- [static let backTab: NSEvent.SpecialKey](./specialkey-swift.struct/backtab.md)
  The back tab key.
- [static let tab: NSEvent.SpecialKey](./specialkey-swift.struct/tab.md)
  The tab key.
### Getting the Navigation-Related Keys
- [static let upArrow: NSEvent.SpecialKey](./specialkey-swift.struct/uparrow.md)
  The up arrow key.
- [static let downArrow: NSEvent.SpecialKey](./specialkey-swift.struct/downarrow.md)
  The down arrow key.
- [static let leftArrow: NSEvent.SpecialKey](./specialkey-swift.struct/leftarrow.md)
  The left arrow key.
- [static let rightArrow: NSEvent.SpecialKey](./specialkey-swift.struct/rightarrow.md)
  The right arrow key.
- [static let pageUp: NSEvent.SpecialKey](./specialkey-swift.struct/pageup.md)
  The page up key.
- [static let pageDown: NSEvent.SpecialKey](./specialkey-swift.struct/pagedown.md)
  The page down key.
- [static let home: NSEvent.SpecialKey](./specialkey-swift.struct/home.md)
  The home key.
- [static let end: NSEvent.SpecialKey](./specialkey-swift.struct/end.md)
  The end key.
- [static let prev: NSEvent.SpecialKey](./specialkey-swift.struct/prev.md)
  The previous key.
- [static let next: NSEvent.SpecialKey](./specialkey-swift.struct/next.md)
  The next key.
### Getting Special Behavior Keys
- [static let begin: NSEvent.SpecialKey](./specialkey-swift.struct/begin.md)
  The begin key.
- [static let `break`: NSEvent.SpecialKey](./specialkey-swift.struct/break.md)
  The break key.
- [static let clearDisplay: NSEvent.SpecialKey](./specialkey-swift.struct/cleardisplay.md)
  The clear display key.
- [static let clearLine: NSEvent.SpecialKey](./specialkey-swift.struct/clearline.md)
  The clear line key.
- [static let deleteCharacter: NSEvent.SpecialKey](./specialkey-swift.struct/deletecharacter.md)
  The delete character key.
- [static let deleteLine: NSEvent.SpecialKey](./specialkey-swift.struct/deleteline.md)
  The delete line key.
- [static let execute: NSEvent.SpecialKey](./specialkey-swift.struct/execute.md)
  The execute key.
- [static let find: NSEvent.SpecialKey](./specialkey-swift.struct/find.md)
  The find key.
- [static let formFeed: NSEvent.SpecialKey](./specialkey-swift.struct/formfeed.md)
  The form feed key.
- [static let help: NSEvent.SpecialKey](./specialkey-swift.struct/help.md)
  The help key.
- [static let insert: NSEvent.SpecialKey](./specialkey-swift.struct/insert.md)
  The insert key.
- [static let insertCharacter: NSEvent.SpecialKey](./specialkey-swift.struct/insertcharacter.md)
  The insert character key.
- [static let insertLine: NSEvent.SpecialKey](./specialkey-swift.struct/insertline.md)
  The insert line key.
- [static let lineSeparator: NSEvent.SpecialKey](./specialkey-swift.struct/lineseparator.md)
  The line separator key.
- [static let menu: NSEvent.SpecialKey](./specialkey-swift.struct/menu.md)
  The menu key.
- [static let modeSwitch: NSEvent.SpecialKey](./specialkey-swift.struct/modeswitch.md)
  The mode switch key.
- [static let paragraphSeparator: NSEvent.SpecialKey](./specialkey-swift.struct/paragraphseparator.md)
  The paragraph separator key.
- [static let pause: NSEvent.SpecialKey](./specialkey-swift.struct/pause.md)
  The pause key.
- [static let print: NSEvent.SpecialKey](./specialkey-swift.struct/print.md)
  The print key.
- [static let printScreen: NSEvent.SpecialKey](./specialkey-swift.struct/printscreen.md)
  The print screen key.
- [static let redo: NSEvent.SpecialKey](./specialkey-swift.struct/redo.md)
  The redo key.
- [static let reset: NSEvent.SpecialKey](./specialkey-swift.struct/reset.md)
  The reset key.
- [static let scrollLock: NSEvent.SpecialKey](./specialkey-swift.struct/scrolllock.md)
  The scroll lock key.
- [static let select: NSEvent.SpecialKey](./specialkey-swift.struct/select.md)
  The select key.
- [static let stop: NSEvent.SpecialKey](./specialkey-swift.struct/stop.md)
  The stop key.
- [static let sysReq: NSEvent.SpecialKey](./specialkey-swift.struct/sysreq.md)
  The system request key.
- [static let system: NSEvent.SpecialKey](./specialkey-swift.struct/system.md)
  The system key.
- [static let undo: NSEvent.SpecialKey](./specialkey-swift.struct/undo.md)
  The undo key.
- [static let user: NSEvent.SpecialKey](./specialkey-swift.struct/user.md)
  The user key.
### Getting the Function Keys
- [static let f1: NSEvent.SpecialKey](./specialkey-swift.struct/f1.md)
  The F1 key.
- [static let f2: NSEvent.SpecialKey](./specialkey-swift.struct/f2.md)
  The F2 key.
- [static let f3: NSEvent.SpecialKey](./specialkey-swift.struct/f3.md)
  The F3 key.
- [static let f4: NSEvent.SpecialKey](./specialkey-swift.struct/f4.md)
  The F4 key.
- [static let f5: NSEvent.SpecialKey](./specialkey-swift.struct/f5.md)
  The F5 key.
- [static let f6: NSEvent.SpecialKey](./specialkey-swift.struct/f6.md)
  The F6 key.
- [static let f7: NSEvent.SpecialKey](./specialkey-swift.struct/f7.md)
  The F7 key.
- [static let f8: NSEvent.SpecialKey](./specialkey-swift.struct/f8.md)
  The F8 key.
- [static let f9: NSEvent.SpecialKey](./specialkey-swift.struct/f9.md)
  The F9 key.
- [static let f10: NSEvent.SpecialKey](./specialkey-swift.struct/f10.md)
  The F10 key.
- [static let f11: NSEvent.SpecialKey](./specialkey-swift.struct/f11.md)
  The F11 key.
- [static let f12: NSEvent.SpecialKey](./specialkey-swift.struct/f12.md)
  The F12 key.
- [static let f13: NSEvent.SpecialKey](./specialkey-swift.struct/f13.md)
  The F13 key.
- [static let f14: NSEvent.SpecialKey](./specialkey-swift.struct/f14.md)
  The F14 key.
- [static let f15: NSEvent.SpecialKey](./specialkey-swift.struct/f15.md)
  The F15 key.
- [static let f16: NSEvent.SpecialKey](./specialkey-swift.struct/f16.md)
  The F16 key.
- [static let f17: NSEvent.SpecialKey](./specialkey-swift.struct/f17.md)
  The F17 key.
- [static let f18: NSEvent.SpecialKey](./specialkey-swift.struct/f18.md)
  The F18 key.
- [static let f19: NSEvent.SpecialKey](./specialkey-swift.struct/f19.md)
  The F19 key.
- [static let f20: NSEvent.SpecialKey](./specialkey-swift.struct/f20.md)
  The F20 key.
- [static let f21: NSEvent.SpecialKey](./specialkey-swift.struct/f21.md)
  The F21 key.
- [static let f22: NSEvent.SpecialKey](./specialkey-swift.struct/f22.md)
  The F22 key.
- [static let f23: NSEvent.SpecialKey](./specialkey-swift.struct/f23.md)
  The F23 key.
- [static let f24: NSEvent.SpecialKey](./specialkey-swift.struct/f24.md)
  The F24 key.
- [static let f25: NSEvent.SpecialKey](./specialkey-swift.struct/f25.md)
  The F25 key.
- [static let f26: NSEvent.SpecialKey](./specialkey-swift.struct/f26.md)
  The F26 key.
- [static let f27: NSEvent.SpecialKey](./specialkey-swift.struct/f27.md)
  The F27 key.
- [static let f28: NSEvent.SpecialKey](./specialkey-swift.struct/f28.md)
  The F28 key.
- [static let f29: NSEvent.SpecialKey](./specialkey-swift.struct/f29.md)
  The F29 key.
- [static let f30: NSEvent.SpecialKey](./specialkey-swift.struct/f30.md)
  The F30 key.
- [static let f31: NSEvent.SpecialKey](./specialkey-swift.struct/f31.md)
  The F31 key.
- [static let f32: NSEvent.SpecialKey](./specialkey-swift.struct/f32.md)
  The F32 key.
- [static let f33: NSEvent.SpecialKey](./specialkey-swift.struct/f33.md)
  The F33 key.
- [static let f34: NSEvent.SpecialKey](./specialkey-swift.struct/f34.md)
  The F34 key.
- [static let f35: NSEvent.SpecialKey](./specialkey-swift.struct/f35.md)
  The F35 key.
### Getting the Key’s Value
- [var unicodeScalar: Unicode.Scalar](./specialkey-swift.struct/unicodescalar.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Getting key event information
- [var characters: String?](./characters.md)
  The characters associated with a key-up or key-down event.
- [var charactersIgnoringModifiers: String?](./charactersignoringmodifiers.md)
  The characters generated by a key event as if no modifier key (except for Shift) applies.
- [var keyCode: UInt16](./keycode.md)
  The virtual code for the key associated with the event.
- [func characters(byApplyingModifiers: NSEvent.ModifierFlags) -> String?](./characters%28byapplyingmodifiers%29.md)
  Returns the new characters that result if you apply the specified modifier keys to the event.
- [class var keyRepeatDelay: TimeInterval](./keyrepeatdelay.md)
  The number of seconds someone must hold down a key before the first key repeat event occurs.
- [class var keyRepeatInterval: TimeInterval](./keyrepeatinterval.md)
  The number of seconds someone must hold down a key to generate key-repeat events after the initial delay.
- [var specialKey: NSEvent.SpecialKey?](./specialkey-swift.property.md)
  The code associated with a function key or other special key.
- [Function-Key Unicode Values](../function-key-unicode-values.md)
  Constants for reserved keyboard function keys that correspond to unicode characters.
- [var isARepeat: Bool](./isarepeat.md)
  A Boolean value that indicates whether the key event is a repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/specialkey-swift.struct)*