# isResizable

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the column is resizable.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`resizingMask`](./resizingmask.md) instead.

## Declaration

```objc
- (BOOL) isResizable;
```

#### Return Value

[`true`](../../Swift/true.md) if the user is allowed to resize the receiver in its `NSTableView`, [`false`](../../Swift/false.md) otherwise.

#### Discussion

You can change the table column size programmatically regardless of this setting, with the minimum and maximum constraints defined by [`minWidth`](./minwidth.md) and [`maxWidth`](./maxwidth.md).

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
- [- setResizable:](./setresizable_.md)
  Sets whether the user can resize the receiver in its NSTableView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/isresizable)*