# browser(_:nextTypeSelectMatchFromRow:toRow:inColumn:for:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, nextTypeSelectMatchFromRow startRow: Int, toRow endRow: Int, inColumn column: Int, for searchString: String?) -> Int
```

#### Return Value

The index of the first row that matches `searchString` between `startRowIndex` and `endRowIndex` - 1, or `-1` if there is no match.

## Parameters

- `browser`: The browser.
- `startRow`: The beginning of the row set to search.
- `endRow`: The end of the row set to search. This value can be less than   when the search wraps around to the beginning.
- `column`: The column containing the rows being searched.
- `searchString`: The keyboard-based selection string. It is   when no keyboard-based selection has begun.

## See Also

- [func browser(NSBrowser, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](nsbrowserdelegate/browser(_:shouldtypeselectfor:withcurrentsearch:).md)
  Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.
- [func browser(NSBrowser, typeSelectStringForRow: Int, inColumn: Int) -> String?](nsbrowserdelegate/browser(_:typeselectstringforrow:incolumn:).md)
  Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:nexttypeselectmatchfromrow:torow:incolumn:for:))*