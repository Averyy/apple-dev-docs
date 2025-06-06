# browser(_:titleOfColumn:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the title to display above the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, titleOfColumn column: Int) -> String?
```

#### Return Value

The title of the specified column.

## Parameters

- `sender`: The browser.
- `column`: The index the column to be titled.

## See Also

- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](nsbrowserdelegate/browser(_:iscolumnvalid:).md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](nsbrowserdelegate/browser(_:numberofchildrenofitem:).md)
  Asks the delegate for the number of children the given item has.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:titleofcolumn:))*