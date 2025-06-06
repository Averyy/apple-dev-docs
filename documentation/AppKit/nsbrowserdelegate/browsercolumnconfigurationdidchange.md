# browserColumnConfigurationDidChange(_:)

**Framework**: AppKit  
**Kind**: method

Used by clients to implement their own column width persistence.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func browserColumnConfigurationDidChange(_ notification: Notification)
```

#### Discussion

This method applies only to browsers with resize type [`NSBrowser.ColumnResizingType.userColumnResizing`](nsbrowser/columnresizingtype-swift.enum/usercolumnresizing.md). It is invoked when the [`setWidth(_:ofColumn:)`](nsbrowser/setwidth(_:ofcolumn:).md) method of [`NSBrowser`](nsbrowser.md) is used to change the width of any browser columns or when the user resizes any columns. If the user resizes more than one column, a single notification is posted when the user is finished resizing.

## Parameters

- `notification`: A notification named  .

## See Also

- [func setWidth(CGFloat, ofColumn: Int)](nsbrowser/setwidth(_:ofcolumn:).md)
  Sets the width of the specified column.
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:).md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:sizetofitwidthofcolumn:).md)
  Returns the ideal width for a column.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:heightofrow:incolumn:).md)
  Specifies the height of the specified row in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browsercolumnconfigurationdidchange(_:))*