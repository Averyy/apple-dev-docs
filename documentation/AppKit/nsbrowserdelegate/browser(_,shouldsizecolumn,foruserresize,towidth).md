# browser(_:shouldSizeColumn:forUserResize:toWidth:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used to determine a column’s initial size.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, shouldSizeColumn columnIndex: Int, forUserResize: Bool, toWidth suggestedWidth: CGFloat) -> CGFloat
```

```objc
- (CGFloat) browser:(NSBrowser *) browser shouldSizeColumn:(NSInteger) columnIndex forUserResize:(BOOL) forUserResize toWidth:(CGFloat) suggestedWidth;
```

#### Return Value

The delegate’s desired initial width for a newly added column. If you want to accept the suggested width, return `suggestedWidth`. If you return `0` or a size too small to display the resize handle and a portion of the column, the actual size used will be larger than the size you requested.

#### Discussion

This method applies only to browsers with resize type [`NSBrowser.ColumnResizingType.noColumnResizing`](../nsbrowser/columnresizingtype-swift.enum/nocolumnresizing.md) or [`NSBrowser.ColumnResizingType.userColumnResizing`](../nsbrowser/columnresizingtype-swift.enum/usercolumnresizing.md) (see [`NSBrowser.ColumnResizingType`](../nsbrowser/columnresizingtype-swift.enum.md)).

## Parameters

- `browser`: The browser.
- `columnIndex`: The index of the column to size.
- `forUserResize`: Currently, this is always set to [`false`](../../Swift/false.md).
- `suggestedWidth`: The suggested width for the column.

## See Also

### Related Documentation
- [func setWidth(CGFloat, ofColumn: Int)](../nsbrowser/setwidth%28_,ofcolumn%29.md)
  Sets the width of the specified column.
### Sizing
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](./browser%28_,sizetofitwidthofcolumn%29.md)
  Returns the ideal width for a column.
- [func browserColumnConfigurationDidChange(Notification)](./browsercolumnconfigurationdidchange%28_%29.md)
  Used by clients to implement their own column width persistence.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](./browser%28_,heightofrow,incolumn%29.md)
  Specifies the height of the specified row in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:))*