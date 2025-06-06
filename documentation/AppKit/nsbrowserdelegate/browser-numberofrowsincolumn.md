# browser(_:numberOfRowsInColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the number of rows of data in the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, numberOfRowsInColumn column: Int) -> Int
```

#### Return Value

The number of rows of data.

#### Discussion

Either this method or [`browser(_:createRowsForColumn:in:)`](nsbrowserdelegate/browser(_:createrowsforcolumn:in:).md) must be implemented, but not both.

## Parameters

- `sender`: The browser.
- `column`: The index of the column.

## See Also

- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:).md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](nsbrowserdelegate/browser(_:iscolumnvalid:).md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](nsbrowserdelegate/browser(_:numberofchildrenofitem:).md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](nsbrowserdelegate/browser(_:titleofcolumn:).md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:numberofrowsincolumn:))*