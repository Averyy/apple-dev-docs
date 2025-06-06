# getRow(_:column:for:)

**Framework**: AppKit  
**Kind**: method

Gets the row and column coordinates for the specified point, if a cell exists at that point.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func getRow(_ row: UnsafeMutablePointer<Int>?, column: UnsafeMutablePointer<Int>?, for point: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a cell exists at the specified point; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If a row does not exist at `point`, then `-1` is set for the row. If a column does not exist at `point`, then `-1` is set for the column.

## Parameters

- `row`: On output, the row number of the cell at the specified point, or   if there is no cell at the point.
- `column`: On output, he column number of the cell at the specified point, or   if there is no cell at the point.
- `point`: The point to test.

## See Also

- [func frame(ofRow: Int, inColumn: Int) -> NSRect](nsbrowser/frame(ofrow:incolumn:).md)
  Returns the frame of the cell at the specified location, including the expandable arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/getrow(_:column:for:))*