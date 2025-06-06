# browser(_:sizeToFitWidthOfColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the ideal width for a column.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, sizeToFitWidthOfColumn columnIndex: Int) -> CGFloat
```

#### Return Value

The ideal width of the column. This method is used when performing a “right-size” operation, that is, when sizing a column to the smallest width that contains all the content without clipping or truncating.

#### Discussion

If `columnIndex` is `–1`, you should return a size that can be uniformly applied to all columns (that is, every column will be set to this size).

Returning a value of `-1` allows you to opt-out of providing a width for the requested column.

#### Discussion

This method applies only to browsers with resize type [`NSBrowser.ColumnResizingType.userColumnResizing`](nsbrowser/columnresizingtype-swift.enum/usercolumnresizing.md).

It is assumed that the implementation may be expensive, so it will be called only when necessary.

## Parameters

- `browser`: The browser.
- `columnIndex`: The index of the column to size. If  , the result is used to resize all columns.

## See Also

- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:).md)
  Used to determine a column’s initial size.
- [func browserColumnConfigurationDidChange(Notification)](nsbrowserdelegate/browsercolumnconfigurationdidchange(_:).md)
  Used by clients to implement their own column width persistence.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:heightofrow:incolumn:).md)
  Specifies the height of the specified row in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:sizetofitwidthofcolumn:))*