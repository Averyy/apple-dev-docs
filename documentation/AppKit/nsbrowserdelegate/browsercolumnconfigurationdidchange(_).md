# browserColumnConfigurationDidChange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used by clients to implement their own column width persistence.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func browserColumnConfigurationDidChange(_ notification: Notification)
```

```objc
- (void) browserColumnConfigurationDidChange:(NSNotification *) notification;
```

#### Discussion

This method applies only to browsers with resize type [`NSBrowser.ColumnResizingType.userColumnResizing`](../nsbrowser/columnresizingtype-swift.enum/usercolumnresizing.md). It is invoked when the [`setWidth(_:ofColumn:)`](../nsbrowser/setwidth%28_,ofcolumn%29.md) method of [`NSBrowser`](../nsbrowser.md) is used to change the width of any browser columns or when the user resizes any columns. If the user resizes more than one column, a single notification is posted when the user is finished resizing.

## Parameters

- `notification`: A notification named [`columnConfigurationDidChangeNotification`](../nsbrowser/columnconfigurationdidchangenotification.md).

## See Also

### Related Documentation
- [func setWidth(CGFloat, ofColumn: Int)](../nsbrowser/setwidth%28_,ofcolumn%29.md)
  Sets the width of the specified column.
### Sizing
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](./browser%28_,shouldsizecolumn,foruserresize,towidth%29.md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](./browser%28_,sizetofitwidthofcolumn%29.md)
  Returns the ideal width for a column.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](./browser%28_,heightofrow,incolumn%29.md)
  Specifies the height of the specified row in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browsercolumnconfigurationdidchange(_:))*