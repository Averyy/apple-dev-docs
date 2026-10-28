# browser(_:numberOfChildrenOfItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the number of children the given item has.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, numberOfChildrenOfItem item: Any?) -> Int
```

```objc
- (NSInteger) browser:(NSBrowser *) browser numberOfChildrenOfItem:(id) item;
```

## Return Value

The number of children.

## Parameters

- `browser`: The browser.
- `item`: The item that has some number of children.

## See Also

### Getting Browser Information
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](./browser%28_,iscolumnvalid%29.md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](./browser%28_,numberofrowsincolumn%29.md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](./browser%28_,titleofcolumn%29.md)
  Asks the delegate for the title to display above the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:numberofchildrenofitem:))*