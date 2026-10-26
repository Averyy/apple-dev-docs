# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated properties
- [var controlTint: NSControlTint](./nscell/controltint.md)
  The cell’s control tint.
### Deprecated type aliases
- [typealias StateValue](./nscell/statevalue.md)
  Constants for specifying a cell’s state and are used mostly for buttons.
### Deprecated constants
- [class let currentControlTintDidChangeNotification: NSNotification.Name](./nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.
### Deprecated methods
- [- setEntryType:](./nscell/setentrytype_.md)
  Sets how numeric data is formatted in the receiver and places restrictions on acceptable input.
- [- entryType](./nscell/entrytype.md)
  Returns the type of data the user can type into the receiver.
- [- isEntryAcceptable:](./nscell/isentryacceptable_.md)
  Returns whether a string representing a numeric or date value is formatted in a suitable way for the cell’s entry type.
- [- setFloatingPointFormat:left:right:](./nscell/setfloatingpointformat_left_right_.md)
  Sets the auto-ranging and floating point number format of the receiver’s cell.
- [- setTitleWithMnemonic:](./nscell/settitlewithmnemonic_.md)
  Sets the title of the receiver with one character in the string denoted as an access key.
- [- mnemonic](./nscell/mnemonic.md)
  Returns the character in the receiver’s title that appears underlined for use as a mnemonic.
- [- setMnemonicLocation:](./nscell/setmnemoniclocation_.md)
  Sets the character of the receiver’s title to be used as a mnemonic character.
- [- mnemonicLocation](./nscell/mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell-deprecated-symbols)*