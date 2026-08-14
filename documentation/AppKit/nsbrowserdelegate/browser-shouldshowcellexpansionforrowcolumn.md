# browser(_:shouldShowCellExpansionForRow:column:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow the delegate to control cell expansion for a specific row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, shouldShowCellExpansionForRow row: Int, column: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow the cell expansion tooltip; [`false`](https://developer.apple.com/documentation/swift/false) to disallow it.

#### Discussion

Cell expansion can occur when the mouse hovers over the specified cell and the cell contents are unable to be fully displayed within the cell. If this method returns YES, the full cell contents will be shown in a special floating tool tip view, otherwise the content is truncated.

## Parameters

- `browser`: The browser.
- `row`: The index of the row requesting an expansion tooltip.
- `column`: The index of the column containing the requesting row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:shouldshowcellexpansionforrow:column:))*