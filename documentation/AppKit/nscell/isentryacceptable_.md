# isEntryAcceptable:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether a string representing a numeric or date value is formatted in a suitable way for the cell’s entry type.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

> **Deprecated**: Use [`Formatter`](../../Foundation/formatter.md) instead.

## Declaration

```objc
- (BOOL) isEntryAcceptable:(NSString *) string;
```

## Return Value

[`true`](../../Swift/true.md) if `aString` is formatted appropriately for the receiver, otherwise [`false`](../../Swift/false.md).

## Parameters

- `string`: A string containing the numeric or date value.

## See Also

### Deprecated methods
- [- setEntryType:](./setentrytype_.md)
  Sets how numeric data is formatted in the receiver and places restrictions on acceptable input.
- [- entryType](./entrytype.md)
  Returns the type of data the user can type into the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isentryacceptable:)*