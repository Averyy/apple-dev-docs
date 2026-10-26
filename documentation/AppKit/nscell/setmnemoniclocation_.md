# setMnemonicLocation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the character of the receiver’s title to be used as a mnemonic character.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Mnemonics are not used.

## Declaration

```objc
- (void) setMnemonicLocation:(NSUInteger) location;
```

#### Discussion

Mnemonics are not supported in macOS.

## Parameters

- `location`: The zero-based index into the cell’s title string specifying the location of the mnemonic character. The specified character is underlined when the title is drawn.

## See Also

### Deprecated methods
- [- setEntryType:](./setentrytype_.md)
  Sets how numeric data is formatted in the receiver and places restrictions on acceptable input.
- [- entryType](./entrytype.md)
  Returns the type of data the user can type into the receiver.
- [- isEntryAcceptable:](./isentryacceptable_.md)
  Returns whether a string representing a numeric or date value is formatted in a suitable way for the cell’s entry type.
- [- setFloatingPointFormat:left:right:](./setfloatingpointformat_left_right_.md)
  Sets the auto-ranging and floating point number format of the receiver’s cell.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title of the receiver with one character in the string denoted as an access key.
- [- mnemonic](./mnemonic.md)
  Returns the character in the receiver’s title that appears underlined for use as a mnemonic.
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setmnemoniclocation:)*