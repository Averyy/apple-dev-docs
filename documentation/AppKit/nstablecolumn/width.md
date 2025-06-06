# width

**Framework**: AppKit  
**Kind**: property

The table column’s width, in points.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var width: CGFloat { get set }
```

#### Discussion

The default value of this property is `100.0`.

If the value of this property exceeds the minimum or maximum width, it’s adjusted to the appropriate limiting value.

This property posts [`columnDidResizeNotification`](nstableview/columndidresizenotification.md) on behalf of the table column’s `NSTableView` and marks the table view as needing display.

## See Also

- [var minWidth: CGFloat](nstablecolumn/minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](nstablecolumn/maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingmask.md)
  The table column’s resizing mask.
- [func sizeToFit()](nstablecolumn/sizetofit.md)
  Resizes the table column to fit the width of its header cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/width)*