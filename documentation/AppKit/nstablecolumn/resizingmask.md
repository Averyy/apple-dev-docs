# resizingMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table column’s resizing mask.

**Availability**:
- macOS

## Declaration

```swift
var resizingMask: NSTableColumn.ResizingOptions { get set }
```

```objc
@property NSTableColumnResizingOptions resizingMask;
```

## Discussion

The value of this property specifies the resizability of the table column. See [Resizing Modes](../resizing-modes.md) for possible values. Values can be combined using the C bitwise OR operator.

When the value of this property is `0`, the column is not resizable. The default value of this property is [`userResizingMask`](./resizingoptions/userresizingmask.md) | [`autoresizingMask`](./resizingoptions/autoresizingmask.md).

## See Also

### Controlling Size
- [var width: CGFloat](./width.md)
  The table column’s width, in points.
- [var minWidth: CGFloat](./minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](./maxwidth.md)
  The table column’s maximum width, in points.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes the table column to fit the width of its header cell.
- [- isResizable](./isresizable.md)
  Returns whether the column is resizable.
- [- setResizable:](./setresizable_.md)
  Sets whether the user can resize the receiver in its NSTableView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingmask)*