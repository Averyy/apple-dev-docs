# sizeToFit()

**Framework**: AppKit  
**Kind**: method

Resizes the table column to fit the width of its header cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sizeToFit()
```

#### Discussion

If the table column’s maximum width is less than the width of the header, the maximum is increased to the header’s width. Similarly, if the table column’s minimum width is greater than the width of the header, the minimum is reduced to the header’s width.

If this method causes the table column’s width to change, the column’s table view is marked as needing display.

## See Also

- [var width: CGFloat](nstablecolumn/width.md)
  The table column’s width, in points.
- [var minWidth: CGFloat](nstablecolumn/minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](nstablecolumn/maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingmask.md)
  The table column’s resizing mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/sizetofit())*