# browser(_:willDisplayCell:atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, willDisplayCell cell: Any, atRow row: Int, column: Int)
```

```objc
- (void) browser:(NSBrowser *) sender willDisplayCell:(id) cell atRow:(NSInteger) row column:(NSInteger) column;
```

## Discussion

The delegate should set any state necessary for the correct display of the cell.

## Parameters

- `sender`: The browser.
- `cell`: The cell to be displayed.
- `row`: The row index of the cell to be displayed.
- `column`: The column index of the cell to be displayed.

## See Also

### Related Documentation
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](./browser%28_,numberofrowsincolumn%29.md)
  Returns the number of rows of data in the specified column.
### Managing Columns
- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](./browser%28_,createrowsforcolumn,in%29.md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](./browser%28_,didchangelastcolumn,tocolumn%29.md)
  Tells the delegate that the browser’s last column changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:))*