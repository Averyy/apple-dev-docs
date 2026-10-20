# browser(_:numberOfRowsInColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of rows of data in the specified column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, numberOfRowsInColumn column: Int) -> Int
```

```objc
- (NSInteger) browser:(NSBrowser *) sender numberOfRowsInColumn:(NSInteger) column;
```

#### Return Value

The number of rows of data.

#### Discussion

Either this method or [`browser(_:createRowsForColumn:in:)`](./browser%28_,createrowsforcolumn,in%29.md) must be implemented, but not both.

## Parameters

- `sender`: The browser.
- `column`: The index of the column.

## See Also

### Related Documentation
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](./browser%28_,willdisplaycell,atrow,column%29.md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
### Getting Browser Information
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](./browser%28_,iscolumnvalid%29.md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](./browser%28_,numberofchildrenofitem%29.md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](./browser%28_,titleofcolumn%29.md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:numberofrowsincolumn:))*