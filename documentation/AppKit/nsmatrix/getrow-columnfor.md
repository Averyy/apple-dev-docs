# getRow(_:column:for:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the specified point lies within one of the cells of the matrix and returns the location of the cell within which the point lies.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func getRow(_ row: UnsafeMutablePointer<Int>, column col: UnsafeMutablePointer<Int>, for point: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the point lies within one of the cells in the receiver; [`false`](https://developer.apple.com/documentation/Swift/false) if the point falls outside the bounds of the receiver or lies within an intercell spacing.

## Parameters

- `row`: On return, the row of the cell containing the specified point.
- `col`: On return, the column of the cell containing the specified point.
- `point`: The point to locate; this point should be in the coordinate system of the receiver.

## See Also

- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, of: NSCell) -> Bool](nsmatrix/getrow(_:column:of:).md)
  Searches the receiver for the specified cell and returns the row and column of the cell


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/getrow(_:column:for:))*