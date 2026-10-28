# browser(_:createRowsForColumn:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a row in the given matrix for each row of data in the specified column of the browser.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, createRowsForColumn column: Int, in matrix: NSMatrix)
```

```objc
- (void) browser:(NSBrowser *) sender createRowsForColumn:(NSInteger) column inMatrix:(NSMatrix *) matrix;
```

## Discussion

Either this method or [`browser(_:numberOfRowsInColumn:)`](./browser%28_,numberofrowsincolumn%29.md) must be implemented, but not both, or an [`NSBrowserIllegalDelegateException`](../nsbrowserillegaldelegateexception.md) will be raised.

## Parameters

- `sender`: The browser.
- `column`: The index of the column in which the rows are located.
- `matrix`: The matrix in which the rows are created.

## See Also

### Managing Columns
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](./browser%28_,willdisplaycell,atrow,column%29.md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](./browser%28_,didchangelastcolumn,tocolumn%29.md)
  Tells the delegate that the browser’s last column changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:createrowsforcolumn:in:))*