# browser(_:titleOfColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the title to display above the specified column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, titleOfColumn column: Int) -> String?
```

```objc
- (NSString *) browser:(NSBrowser *) sender titleOfColumn:(NSInteger) column;
```

## Return Value

The title of the specified column.

## Parameters

- `sender`: The browser.
- `column`: The index the column to be titled.

## See Also

### Related Documentation
- [func setTitle(String, ofColumn: Int)](../nsbrowser/settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [func title(ofColumn: Int) -> String?](../nsbrowser/title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
### Getting Browser Information
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](./browser%28_,iscolumnvalid%29.md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](./browser%28_,numberofrowsincolumn%29.md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](./browser%28_,numberofchildrenofitem%29.md)
  Asks the delegate for the number of children the given item has.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:titleofcolumn:))*