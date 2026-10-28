# browser(_:isColumnValid:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the contents of the specified column are valid.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, isColumnValid column: Int) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) sender isColumnValid:(NSInteger) column;
```

## Return Value

[`true`](../../Swift/true.md) if the column’s contents are valid; otherwise, [`false`](../../Swift/false.md). If [`false`](../../Swift/false.md) is returned, `sender` reloads the column.

## Discussion

This method is invoked in response to the [`validateVisibleColumns()`](../nsbrowser/validatevisiblecolumns%28%29.md)method of [`NSBrowser`](../nsbrowser.md) being sent to `sender`.

## Parameters

- `sender`: The browser containing the column to validate.
- `column`: The index of the column to validate.

## See Also

### Getting Browser Information
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](./browser%28_,numberofrowsincolumn%29.md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](./browser%28_,numberofchildrenofitem%29.md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](./browser%28_,titleofcolumn%29.md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:iscolumnvalid:))*