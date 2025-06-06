# browser(_:typeSelectStringForRow:inColumn:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, typeSelectStringForRow row: Int, inColumn column: Int) -> String?
```

#### Return Value

The keyboard-based selection string.

#### Discussion

Returning the empty string or `nil` (for example, when the cell does not contain text) specifies that the `[``column`, `row``]` cell has no text to search.

If the delegate does not implement this method, all cells with text are searched, and the browser determines the keyboard-based selection text by sending [`stringValue`](nscell/stringvalue.md) to the cell specified by `column` and `row`.

## Parameters

- `browser`: The browser.
- `row`: The row index.
- `column`: The column index.

## See Also

- [func browser(NSBrowser, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](nsbrowserdelegate/browser(_:shouldtypeselectfor:withcurrentsearch:).md)
  Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.
- [func browser(NSBrowser, nextTypeSelectMatchFromRow: Int, toRow: Int, inColumn: Int, for: String?) -> Int](nsbrowserdelegate/browser(_:nexttypeselectmatchfromrow:torow:incolumn:for:).md)
  Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:typeselectstringforrow:incolumn:))*