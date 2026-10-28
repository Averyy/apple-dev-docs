# browser(_:shouldTypeSelectFor:withCurrentSearch:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, shouldTypeSelectFor event: NSEvent, withCurrentSearch searchString: String?) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) browser shouldTypeSelectForEvent:(NSEvent *) event withCurrentSearchString:(NSString *) searchString;
```

## Return Value

[`true`](../../Swift/true.md) to allow the selection; [`false`](../../Swift/false.md) to disallow it.

## Parameters

- `browser`: The browser.
- `event`: The keyboard event being processed.
- `searchString`: The keyboard-based selection string. It is `nil` when no keyboard-based selection has begun.

## See Also

### Related Documentation
- [var allowsTypeSelect: Bool](../nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).
### Managing Selection Behavior
- [func browser(NSBrowser, typeSelectStringForRow: Int, inColumn: Int) -> String?](./browser%28_,typeselectstringforrow,incolumn%29.md)
  Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.
- [func browser(NSBrowser, nextTypeSelectMatchFromRow: Int, toRow: Int, inColumn: Int, for: String?) -> Int](./browser%28_,nexttypeselectmatchfromrow,torow,incolumn,for%29.md)
  Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:shouldtypeselectfor:withcurrentsearch:))*