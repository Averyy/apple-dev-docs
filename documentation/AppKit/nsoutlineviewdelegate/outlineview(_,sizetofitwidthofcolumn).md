# outlineView(_:sizeToFitWidthOfColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, sizeToFitWidthOfColumn column: Int) -> CGFloat
```

```objc
- (CGFloat) outlineView:(NSOutlineView *) outlineView sizeToFitWidthOfColumn:(NSInteger) column;
```

#### Return Value

The width of the specified column.

#### Discussion

By default, `NSOutlineView` iterates every row in the table, accesses a cell via [`preparedCell(atColumn:row:)`](../nstableview/preparedcell%28atcolumn,row%29.md), and requests the [`cellSize`](../nscell/cellsize.md) to find the appropriate largest width to use.

For accurate results and performance, it is recommended that this method is implemented when using large tables. By default, large tables use a monte carlo simulation instead of iterating every row.

## Parameters

- `outlineView`: The outline view that sent the message.
- `column`: The index of the column.

## See Also

### Customizing Column and Row Sizes
- [func outlineView(NSOutlineView, heightOfRowByItem: Any) -> CGFloat](./outlineview%28_,heightofrowbyitem%29.md)
  Returns the height in points of the row containing `item`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:sizetofitwidthofcolumn:))*