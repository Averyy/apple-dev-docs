# Function-Key Unicode Values

**Framework**: AppKit

Constants for reserved keyboard function keys that correspond to unicode characters.

#### Overview

These constants correspond to unicode characters in the range (0xF700–0xF8FF) and are values you can use with the [`characters`](nsevent/characters.md) and [`charactersIgnoringModifiers`](nsevent/charactersignoringmodifiers.md) properties of the event. You can also use them in some parameters in the [`keyEvent(with:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:)`](nsevent/keyevent(with:location:modifierflags:timestamp:windownumber:context:characters:charactersignoringmodifiers:isarepeat:keycode:).md) method of the event.

Note that the system handles some function keys at a lower level and your app never sees them. Examples include the Volume Up key, Volume Down key, Volume Mute key, Eject key, and Function key found on many Macs.

## Topics

### Getting Common Control Keys
- [var NSDeleteFunctionKey: Int](nsdeletefunctionkey.md)
  The forward delete key.
### Getting the Navigation-Related Keys
- [var NSUpArrowFunctionKey: Int](nsuparrowfunctionkey.md)
  The up arrow key.
- [var NSDownArrowFunctionKey: Int](nsdownarrowfunctionkey.md)
  The down arrow key.
- [var NSLeftArrowFunctionKey: Int](nsleftarrowfunctionkey.md)
  The left arrow key.
- [var NSRightArrowFunctionKey: Int](nsrightarrowfunctionkey.md)
  The right arrow key.
- [var NSPageUpFunctionKey: Int](nspageupfunctionkey.md)
  The page up key.
- [var NSPageDownFunctionKey: Int](nspagedownfunctionkey.md)
  The page down key.
- [var NSHomeFunctionKey: Int](nshomefunctionkey.md)
  The home key.
- [var NSEndFunctionKey: Int](nsendfunctionkey.md)
  The end key.
- [var NSPrevFunctionKey: Int](nsprevfunctionkey.md)
  Previous key.
- [var NSNextFunctionKey: Int](nsnextfunctionkey.md)
  The next key.
### Getting Special Behavior Keys
- [var NSBeginFunctionKey: Int](nsbeginfunctionkey.md)
  The begin key.
- [var NSBreakFunctionKey: Int](nsbreakfunctionkey.md)
  The break key.
- [var NSClearDisplayFunctionKey: Int](nscleardisplayfunctionkey.md)
  The clear display key.
- [var NSClearLineFunctionKey: Int](nsclearlinefunctionkey.md)
  The clear or num lock key.
- [var NSDeleteCharFunctionKey: Int](nsdeletecharfunctionkey.md)
  The delete character key.
- [var NSDeleteLineFunctionKey: Int](nsdeletelinefunctionkey.md)
  The delete line key.
- [var NSExecuteFunctionKey: Int](nsexecutefunctionkey.md)
  The execute key.
- [var NSFindFunctionKey: Int](nsfindfunctionkey.md)
  The find key.
- [var NSHelpFunctionKey: Int](nshelpfunctionkey.md)
  The help key.
- [var NSInsertFunctionKey: Int](nsinsertfunctionkey.md)
  The insert key.
- [var NSInsertCharFunctionKey: Int](nsinsertcharfunctionkey.md)
  The insert character key.
- [var NSInsertLineFunctionKey: Int](nsinsertlinefunctionkey.md)
  The insert line key.
- [var NSMenuFunctionKey: Int](nsmenufunctionkey.md)
  The menu key.
- [var NSModeSwitchFunctionKey: Int](nsmodeswitchfunctionkey.md)
  The mode switch key.
- [var NSPauseFunctionKey: Int](nspausefunctionkey.md)
  The pause key.
- [var NSPrintFunctionKey: Int](nsprintfunctionkey.md)
  The print key.
- [var NSPrintScreenFunctionKey: Int](nsprintscreenfunctionkey.md)
  The print screen key.
- [var NSRedoFunctionKey: Int](nsredofunctionkey.md)
  The redo key.
- [var NSResetFunctionKey: Int](nsresetfunctionkey.md)
  The reset key.
- [var NSScrollLockFunctionKey: Int](nsscrolllockfunctionkey.md)
  The scroll lock key.
- [var NSSelectFunctionKey: Int](nsselectfunctionkey.md)
  The select key.
- [var NSStopFunctionKey: Int](nsstopfunctionkey.md)
  The stop key.
- [var NSSysReqFunctionKey: Int](nssysreqfunctionkey.md)
  The system request key.
- [var NSSystemFunctionKey: Int](nssystemfunctionkey.md)
  The system key.
- [var NSUndoFunctionKey: Int](nsundofunctionkey.md)
  The undo key.
- [var NSUserFunctionKey: Int](nsuserfunctionkey.md)
  The user key.
### Getting the Function Keys
- [var NSF1FunctionKey: Int](nsf1functionkey.md)
  The F1 key.
- [var NSF2FunctionKey: Int](nsf2functionkey.md)
  The F2 key.
- [var NSF3FunctionKey: Int](nsf3functionkey.md)
  The F3 key.
- [var NSF4FunctionKey: Int](nsf4functionkey.md)
  The F4 key.
- [var NSF5FunctionKey: Int](nsf5functionkey.md)
  The F5 key.
- [var NSF6FunctionKey: Int](nsf6functionkey.md)
  The F6 key.
- [var NSF7FunctionKey: Int](nsf7functionkey.md)
  The F7 key.
- [var NSF8FunctionKey: Int](nsf8functionkey.md)
  The F8 key.
- [var NSF9FunctionKey: Int](nsf9functionkey.md)
  The F9 key.
- [var NSF10FunctionKey: Int](nsf10functionkey.md)
  The F10 key.
- [var NSF11FunctionKey: Int](nsf11functionkey.md)
  The F11 key.
- [var NSF12FunctionKey: Int](nsf12functionkey.md)
  The F12 key.
- [var NSF13FunctionKey: Int](nsf13functionkey.md)
  The F13 key.
- [var NSF14FunctionKey: Int](nsf14functionkey.md)
  The F14 key.
- [var NSF15FunctionKey: Int](nsf15functionkey.md)
  The F15 key.
- [var NSF16FunctionKey: Int](nsf16functionkey.md)
  The F16 key.
- [var NSF17FunctionKey: Int](nsf17functionkey.md)
  The F17 key.
- [var NSF18FunctionKey: Int](nsf18functionkey.md)
  The F18 key.
- [var NSF19FunctionKey: Int](nsf19functionkey.md)
  The F19 key.
- [var NSF20FunctionKey: Int](nsf20functionkey.md)
  The F20 key.
- [var NSF21FunctionKey: Int](nsf21functionkey.md)
  The F21 key.
- [var NSF22FunctionKey: Int](nsf22functionkey.md)
  The F22 key.
- [var NSF23FunctionKey: Int](nsf23functionkey.md)
  The F23 key.
- [var NSF24FunctionKey: Int](nsf24functionkey.md)
  The F24 key.
- [var NSF25FunctionKey: Int](nsf25functionkey.md)
  The F25 key.
- [var NSF26FunctionKey: Int](nsf26functionkey.md)
  The F26 key.
- [var NSF27FunctionKey: Int](nsf27functionkey.md)
  The F27 key.
- [var NSF28FunctionKey: Int](nsf28functionkey.md)
  The F28 key.
- [var NSF29FunctionKey: Int](nsf29functionkey.md)
  The F29 key.
- [var NSF30FunctionKey: Int](nsf30functionkey.md)
  The F30 key.
- [var NSF31FunctionKey: Int](nsf31functionkey.md)
  The F31 key.
- [var NSF32FunctionKey: Int](nsf32functionkey.md)
  The F32 key.
- [var NSF33FunctionKey: Int](nsf33functionkey.md)
  The F33 key.
- [var NSF34FunctionKey: Int](nsf34functionkey.md)
  The F34 key.
- [var NSF35FunctionKey: Int](nsf35functionkey.md)
  The F35 key.

## See Also

- [var characters: String?](nsevent/characters.md)
  The characters associated with a key-up or key-down event.
- [var charactersIgnoringModifiers: String?](nsevent/charactersignoringmodifiers.md)
  The characters generated by a key event as if no modifier key (except for Shift) applies.
- [var keyCode: UInt16](nsevent/keycode.md)
  The virtual code for the key associated with the event.
- [func characters(byApplyingModifiers: NSEvent.ModifierFlags) -> String?](nsevent/characters(byapplyingmodifiers:).md)
  Returns the new characters that result if you apply the specified modifier keys to the event.
- [class var keyRepeatDelay: TimeInterval](nsevent/keyrepeatdelay.md)
  The number of seconds someone must hold down a key before the first key repeat event occurs.
- [class var keyRepeatInterval: TimeInterval](nsevent/keyrepeatinterval.md)
  The number of seconds someone must hold down a key to generate key-repeat events after the initial delay.
- [var specialKey: NSEvent.SpecialKey?](nsevent/specialkey-swift.property.md)
  The code associated with a function key or other special key.
- [NSEvent.SpecialKey](nsevent/specialkey-swift.struct.md)
  Constants for reserved function keys on the keyboard.
- [var isARepeat: Bool](nsevent/isarepeat.md)
  A Boolean value that indicates whether the key event is a repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/function-key-unicode-values)*