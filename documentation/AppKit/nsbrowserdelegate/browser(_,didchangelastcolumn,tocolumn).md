# browser(_:didChangeLastColumn:toColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the browser’s last column changed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, didChangeLastColumn oldLastColumn: Int, toColumn column: Int)
```

```objc
- (void) browser:(NSBrowser *) browser didChangeLastColumn:(NSInteger) oldLastColumn toColumn:(NSInteger) column;
```

## Parameters

- `browser`: The browser.
- `oldLastColumn`: The index of the old last column.
- `column`: The index of the new last column.

## See Also

### Managing Columns
- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](./browser%28_,createrowsforcolumn,in%29.md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](./browser%28_,willdisplaycell,atrow,column%29.md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:didchangelastcolumn:tocolumn:))*