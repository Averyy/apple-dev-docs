# setFloatingPointFormat:left:right:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the auto-ranging and floating point number format of the receiver’s cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

## Declaration

```objc
- (void) setFloatingPointFormat:(BOOL) autoRange left:(NSUInteger) leftDigits right:(NSUInteger) rightDigits;
```

## Discussion

For more information about auto-ranging and how it works, see the description of this method in the [`NSCell`](../nscell.md) class specification. If the cell is being edited, the current edits are discarded and the cell’s interior is redrawn.

> **Note**:  This method is being deprecated in favor of a new class of formatter objects. For more information, see [`Formatter`](../../Foundation/formatter.md). This documentation is provided only for developers who need to modify older applications.

## Parameters

- `autoRange`: [`true`](../../Swift/true.md) to enable auto-ranging; otherwise, [`false`](../../Swift/false.md).
- `leftDigits`: The number of digits to display to the left of the decimal point.
- `rightDigits`: The number of digits to display to the right of the decimal point.

## See Also

### Related Documentation
- [- setFloatingPointFormat:left:right:](../nscell/setfloatingpointformat_left_right_.md)
  Sets the auto-ranging and floating point number format of the receiver’s cell.
### Deprecated
- [Deprecated symbols](../nscontrol-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/setfloatingpointformat:left:right:)*