# browser(_:shouldTypeSelectFor:withCurrentSearch:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, shouldTypeSelectFor event: NSEvent, withCurrentSearch searchString: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the selection; [`false`](https://developer.apple.com/documentation/Swift/false) to disallow it.

## Parameters

- `browser`: The browser.
- `event`: The keyboard event being processed.
- `searchString`: The keyboard-based selection string. It is   when no keyboard-based selection has begun.

## See Also

- [var allowsTypeSelect: Bool](nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).
- [func browser(NSBrowser, typeSelectStringForRow: Int, inColumn: Int) -> String?](nsbrowserdelegate/browser(_:typeselectstringforrow:incolumn:).md)
  Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.
- [func browser(NSBrowser, nextTypeSelectMatchFromRow: Int, toRow: Int, inColumn: Int, for: String?) -> Int](nsbrowserdelegate/browser(_:nexttypeselectmatchfromrow:torow:incolumn:for:).md)
  Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:shouldtypeselectfor:withcurrentsearch:))*