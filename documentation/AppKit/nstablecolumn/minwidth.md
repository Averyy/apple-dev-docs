# minWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table column’s minimum width, in points.

**Availability**:
- macOS

## Declaration

```swift
var minWidth: CGFloat { get set }
```

```objc
@property CGFloat minWidth;
```

## Discussion

The default value of this property is `10.0`.

The table column width can’t be less than the value of this property, whether the column is resized by the user or programmatically. If the table column’s current width is less than the value of this property, the width is set to the value of this property.

## See Also

### Controlling Size
- [var width: CGFloat](./width.md)
  The table column’s width, in points.
- [var maxWidth: CGFloat](./maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](./resizingmask.md)
  The table column’s resizing mask.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes the table column to fit the width of its header cell.
- [- isResizable](./isresizable.md)
  Returns whether the column is resizable.
- [- setResizable:](./setresizable_.md)
  Sets whether the user can resize the receiver in its NSTableView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/minwidth)*