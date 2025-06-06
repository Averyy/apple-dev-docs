# browser(_:didChangeLastColumn:toColumn:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the browser’s last column changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, didChangeLastColumn oldLastColumn: Int, toColumn column: Int)
```

## Parameters

- `browser`: The browser.
- `oldLastColumn`: The index of the old last column.
- `column`: The index of the new last column.

## See Also

- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](nsbrowserdelegate/browser(_:createrowsforcolumn:in:).md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:).md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:didchangelastcolumn:tocolumn:))*