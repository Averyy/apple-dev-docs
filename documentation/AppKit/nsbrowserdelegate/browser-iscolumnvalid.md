# browser(_:isColumnValid:)

**Framework**: AppKit  
**Kind**: method

Returns whether the contents of the specified column are valid.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, isColumnValid column: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the column’s contents are valid; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). If [`false`](https://developer.apple.com/documentation/swift/false) is returned, `sender` reloads the column.

#### Discussion

This method is invoked in response to the [`validateVisibleColumns()`](nsbrowser/validatevisiblecolumns().md)method of [`NSBrowser`](nsbrowser.md) being sent to `sender`.

## Parameters

- `sender`: The browser containing the column to validate.
- `column`: The index of the column to validate.

## See Also

- [Browser Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Browser/Browser.html#//apple_ref/doc/uid/10000018i)
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](nsbrowserdelegate/browser(_:numberofchildrenofitem:).md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](nsbrowserdelegate/browser(_:titleofcolumn:).md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:iscolumnvalid:))*