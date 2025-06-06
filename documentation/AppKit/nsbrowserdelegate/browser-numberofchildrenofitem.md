# browser(_:numberOfChildrenOfItem:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the number of children the given item has.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, numberOfChildrenOfItem item: Any?) -> Int
```

#### Return Value

The number of children.

## Parameters

- `browser`: The browser.
- `item`: The item that has some number of children.

## See Also

- [func browser(NSBrowser, isColumnValid: Int) -> Bool](nsbrowserdelegate/browser(_:iscolumnvalid:).md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](nsbrowserdelegate/browser(_:titleofcolumn:).md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:numberofchildrenofitem:))*