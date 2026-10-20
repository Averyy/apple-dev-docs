# browser(_:heightOfRow:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the height of the specified row in the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, heightOfRow row: Int, inColumn columnIndex: Int) -> CGFloat
```

```objc
- (CGFloat) browser:(NSBrowser *) browser heightOfRow:(NSInteger) row inColumn:(NSInteger) columnIndex;
```

#### Return Value

The height to set for the specified row, which must be greater than 0.

#### Discussion

The values returned for this method may be cached. Therefore, you should call [`noteHeightOfRowsWithIndexesChanged(_:inColumn:)`](../nsbrowser/noteheightofrowswithindexeschanged%28_,incolumn%29.md) to invalidate a row’s height before changing it.

## Parameters

- `browser`: The browser.
- `row`: The index of the row.
- `columnIndex`: The index of the column.

## See Also

### Sizing
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](./browser%28_,shouldsizecolumn,foruserresize,towidth%29.md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](./browser%28_,sizetofitwidthofcolumn%29.md)
  Returns the ideal width for a column.
- [func browserColumnConfigurationDidChange(Notification)](./browsercolumnconfigurationdidchange%28_%29.md)
  Used by clients to implement their own column width persistence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:heightofrow:incolumn:))*