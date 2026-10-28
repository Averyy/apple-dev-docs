# getRow(_:column:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gets the row and column coordinates for the specified point, if a cell exists at that point.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func getRow(_ row: UnsafeMutablePointer<Int>?, column: UnsafeMutablePointer<Int>?, for point: NSPoint) -> Bool
```

```objc
- (BOOL) getRow:(NSInteger *) row column:(NSInteger *) column forPoint:(NSPoint) point;
```

## Return Value

[`true`](../../Swift/true.md) if a cell exists at the specified point; otherwise, [`false`](../../Swift/false.md).

## Discussion

If a row does not exist at `point`, then `-1` is set for the row. If a column does not exist at `point`, then `-1` is set for the column.

## Parameters

- `row`: On output, the row number of the cell at the specified point, or `-1` if there is no cell at the point.
- `column`: On output, he column number of the cell at the specified point, or `-1` if there is no cell at the point.
- `point`: The point to test.

## See Also

### Getting Row Frames
- [func frame(ofRow: Int, inColumn: Int) -> NSRect](./frame%28ofrow,incolumn%29.md)
  Returns the frame of the cell at the specified location, including the expandable arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/getrow(_:column:for:))*