# setFloatingPointFormat:left:right:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the auto-ranging and floating point number format of the receiver’s cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

> **Deprecated**: Use a formatter instead. See [`formatter`](./formatter.md).

## Declaration

```objc
- (void) setFloatingPointFormat:(BOOL) autoRange left:(NSUInteger) leftDigits right:(NSUInteger) rightDigits;
```

#### Discussion

Sets whether floating-point numbers are auto-ranged in the receiver and sets the sizes of the fields to the left and right of the decimal point. If `autoRange` is [`false`](../../Swift/false.md), `leftDigits` specifies the maximum number of digits to the left of the decimal point, and `rightDigits` specifies the number of digits to the right (the fractional digit places will be padded with zeros to fill this width). However, if a number is too large to fit its integer part in `leftDigits` digits, as many places as are needed on the left are effectively removed from `rightDigits` when the number is displayed.

If `autoRange` is [`true`](../../Swift/true.md), `leftDigits` and `rightDigits` are simply added to form a maximum total field width for the receiver (plus 1 for the decimal point). The fractional part will be padded with zeros on the right to fill this width, or truncated as much as possible (up to removing the decimal point and displaying the number as an integer). The integer portion of a number is never truncated—that is, it is displayed in full no matter what the field width limit is.

The following example sets a cell used to display dollar amounts up to 99,999.99:

```objc
    [[currencyDollarsField cell] setEntryType:NSFloatType];
    [[currencyDollarsField cell] setFloatingPointFormat:NO left:5  right:2];
```

## Parameters

- `autoRange`: If [`true`](../../Swift/true.md), auto-ranging is enabled, otherwise it is disabled.
- `leftDigits`: The number of digits to display to the left of the decimal point.
- `rightDigits`: The number of digits to display to the right of the decimal point.

## See Also

### Deprecated methods
- [- setEntryType:](./setentrytype_.md)
  Sets how numeric data is formatted in the receiver and places restrictions on acceptable input.
- [- entryType](./entrytype.md)
  Returns the type of data the user can type into the receiver.
- [- isEntryAcceptable:](./isentryacceptable_.md)
  Returns whether a string representing a numeric or date value is formatted in a suitable way for the cell’s entry type.
- [- setTitleWithMnemonic:](./settitlewithmnemonic_.md)
  Sets the title of the receiver with one character in the string denoted as an access key.
- [- mnemonic](./mnemonic.md)
  Returns the character in the receiver’s title that appears underlined for use as a mnemonic.
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the receiver’s title to be used as a mnemonic character.
- [- mnemonicLocation](./mnemoniclocation.md)
  Returns the position of the underlined mnemonic character in the receiver’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setfloatingpointformat:left:right:)*