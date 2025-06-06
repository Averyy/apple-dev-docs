# browser(_:willDisplayCell:atRow:column:)

**Framework**: AppKit  
**Kind**: method

Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, willDisplayCell cell: Any, atRow row: Int, column: Int)
```

#### Discussion

The delegate should set any state necessary for the correct display of the cell.

## Parameters

- `sender`: The browser.
- `cell`: The cell to be displayed.
- `row`: The row index of the cell to be displayed.
- `column`: The column index of the cell to be displayed.

## See Also

- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](nsbrowserdelegate/browser(_:createrowsforcolumn:in:).md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](nsbrowserdelegate/browser(_:didchangelastcolumn:tocolumn:).md)
  Tells the delegate that the browser’s last column changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:))*