# minWidth

**Framework**: AppKit  
**Kind**: property

The table column’s minimum width, in points.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var minWidth: CGFloat { get set }
```

#### Discussion

The default value of this property is `10.0`.

The table column width can’t be less than the value of this property, whether the column is resized by the user or programmatically. If the table column’s current width is less than the value of this property, the width is set to the value of this property.

## See Also

- [var width: CGFloat](nstablecolumn/width.md)
  The table column’s width, in points.
- [var maxWidth: CGFloat](nstablecolumn/maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingmask.md)
  The table column’s resizing mask.
- [func sizeToFit()](nstablecolumn/sizetofit.md)
  Resizes the table column to fit the width of its header cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/minwidth)*