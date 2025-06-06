# outlineView(_:nextTypeSelectMatchFromItem:toItem:for:)

**Framework**: AppKit  
**Kind**: method

Returns the first item that matches the searchString from within the range of startItem to endItem

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, nextTypeSelectMatchFromItem startItem: Any, toItem endItem: Any, for searchString: String) -> Any?
```

#### Return Value

The first item—from within the range of `startItem` to `endItem`—that matches the `searchString`, or `nil` if there is no match.

#### Discussion

Implement this method if you want to control how type selection works.  You should include `startItem` as a possible match, but do not include `endItem`.

It is not necessary to implement this method in order to support type select.

## Parameters

- `outlineView`: The outline view that sent the message.
- `startItem`: The first item to search.
- `endItem`: The item before which to stop searching. It is possible for endItem to be less than startItem if the search will wrap.
- `searchString`: The string for which to search.

## See Also

- [func outlineView(NSOutlineView, typeSelectStringFor: NSTableColumn?, item: Any) -> String?](nsoutlineviewdelegate/outlineview(_:typeselectstringfor:item:).md)
  Returns the string that is used for type selection for a given column and item.
- [func outlineView(NSOutlineView, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldtypeselectfor:withcurrentsearch:).md)
  Returns a Boolean value that indicates whether type select should proceed for a given event and search string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:nexttypeselectmatchfromitem:toitem:for:))*