# outlineView(_:shouldTypeSelectFor:withCurrentSearch:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether type select should proceed for a given event and search string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldTypeSelectFor event: NSEvent, withCurrentSearch searchString: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if type select should proceed, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Generally, this method will be called from [`keyDown(with:)`](nsresponder/keydown(with:).md) and the event will be a key event.

## Parameters

- `outlineView`: The outline view that sent the message.
- `event`: The event that caused the message to be sent.
- `searchString`: The string for which searching is to proceed. The search string is   if no type select has begun.

## See Also

- [func outlineView(NSOutlineView, typeSelectStringFor: NSTableColumn?, item: Any) -> String?](nsoutlineviewdelegate/outlineview(_:typeselectstringfor:item:).md)
  Returns the string that is used for type selection for a given column and item.
- [func outlineView(NSOutlineView, nextTypeSelectMatchFromItem: Any, toItem: Any, for: String) -> Any?](nsoutlineviewdelegate/outlineview(_:nexttypeselectmatchfromitem:toitem:for:).md)
  Returns the first item that matches the searchString from within the range of startItem to endItem


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldtypeselectfor:withcurrentsearch:))*