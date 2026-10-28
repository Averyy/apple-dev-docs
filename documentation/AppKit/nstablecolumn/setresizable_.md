# setResizable:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the user can resize the receiver in its NSTableView.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`resizingMask`](./resizingmask.md) instead.

## Declaration

```objc
- (void) setResizable:(BOOL) flag;
```

## Discussion

You can change the table column size programmatically regardless of this setting, with the minimum and maximum constraints defined by [`minWidth`](./minwidth.md) and [`maxWidth`](./maxwidth.md).

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the user can resize the table column; [`false`](../../Swift/false.md) otherwise.

## See Also

### Controlling Size
- [var width: CGFloat](./width.md)
  The table column’s width, in points.
- [var minWidth: CGFloat](./minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](./maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](./resizingmask.md)
  The table column’s resizing mask.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes the table column to fit the width of its header cell.
- [- isResizable](./isresizable.md)
  Returns whether the column is resizable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/setresizable:)*