# width

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table column’s width, in points.

**Availability**:
- macOS

## Declaration

```swift
var width: CGFloat { get set }
```

```objc
@property CGFloat width;
```

#### Discussion

The default value of this property is `100.0`.

If the value of this property exceeds the minimum or maximum width, it’s adjusted to the appropriate limiting value.

This property posts [`columnDidResizeNotification`](../nstableview/columndidresizenotification.md) on behalf of the table column’s `NSTableView` and marks the table view as needing display.

## See Also

### Controlling Size
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
- [- setResizable:](./setresizable_.md)
  Sets whether the user can resize the receiver in its NSTableView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/width)*