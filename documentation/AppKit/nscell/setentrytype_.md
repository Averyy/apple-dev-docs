# setEntryType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets how numeric data is formatted in the receiver and places restrictions on acceptable input.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

> **Deprecated**: Use a formatter instead. See [`formatter`](./formatter.md).

## Declaration

```objc
- (void) setEntryType:(NSInteger) type;
```

## Parameters

- `type`: One of the types listed for this method in [Data Entry Types](../data-entry-types.md).

## See Also

### Deprecated methods
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
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the receiver’s title to be used as a mnemonic character.
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setentrytype:)*