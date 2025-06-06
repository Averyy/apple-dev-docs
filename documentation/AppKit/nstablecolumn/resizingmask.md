# resizingMask

**Framework**: AppKit  
**Kind**: property

The table column’s resizing mask.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var resizingMask: NSTableColumn.ResizingOptions { get set }
```

#### Discussion

The value of this property specifies the resizability of the table column. See [`Resizing Modes`](resizing-modes.md) for possible values. Values can be combined using the C bitwise OR operator.

When the value of this property is `0`, the column is not resizable. The default value of this property is [`userResizingMask`](nstablecolumn/resizingoptions/userresizingmask.md) | [`autoresizingMask`](nstablecolumn/resizingoptions/autoresizingmask.md).

## See Also

- [var width: CGFloat](nstablecolumn/width.md)
  The table column’s width, in points.
- [var minWidth: CGFloat](nstablecolumn/minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](nstablecolumn/maxwidth.md)
  The table column’s maximum width, in points.
- [func sizeToFit()](nstablecolumn/sizetofit.md)
  Resizes the table column to fit the width of its header cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingmask)*