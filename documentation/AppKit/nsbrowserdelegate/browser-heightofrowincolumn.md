# browser(_:heightOfRow:inColumn:)

**Framework**: AppKit  
**Kind**: method

Specifies the height of the specified row in the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, heightOfRow row: Int, inColumn columnIndex: Int) -> CGFloat
```

#### Return Value

The height to set for the specified row, which must be greater than 0.

#### Discussion

The values returned for this method may be cached. Therefore, you should call [`noteHeightOfRowsWithIndexesChanged(_:inColumn:)`](nsbrowser/noteheightofrowswithindexeschanged(_:incolumn:).md) to invalidate a row’s height before changing it.

## Parameters

- `browser`: The browser.
- `row`: The index of the row.
- `columnIndex`: The index of the column.

## See Also

- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:).md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:sizetofitwidthofcolumn:).md)
  Returns the ideal width for a column.
- [func browserColumnConfigurationDidChange(Notification)](nsbrowserdelegate/browsercolumnconfigurationdidchange(_:).md)
  Used by clients to implement their own column width persistence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:heightofrow:incolumn:))*