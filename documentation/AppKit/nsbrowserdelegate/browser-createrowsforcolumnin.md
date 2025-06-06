# browser(_:createRowsForColumn:in:)

**Framework**: AppKit  
**Kind**: method

Creates a row in the given matrix for each row of data in the specified column of the browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, createRowsForColumn column: Int, in matrix: NSMatrix)
```

#### Discussion

Either this method or [`browser(_:numberOfRowsInColumn:)`](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md) must be implemented, but not both, or an [`NSBrowserIllegalDelegateException`](nsbrowserillegaldelegateexception.md) will be raised.

## Parameters

- `sender`: The browser.
- `column`: The index of the column in which the rows are located.
- `matrix`: The matrix in which the rows are created.

## See Also

- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:).md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](nsbrowserdelegate/browser(_:didchangelastcolumn:tocolumn:).md)
  Tells the delegate that the browser’s last column changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:createrowsforcolumn:in:))*