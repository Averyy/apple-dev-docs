# performAction(forItem:)

**Framework**: AppKit  
**Kind**: method

Invoked when the user selects a search result in Help menu.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func performAction(forItem item: Any)
```

#### Discussion

The default implementation brings up Help Viewer for a Help item.

## Parameters

- `item`: An item in the help menu.

## See Also

- [func searchForItems(withSearch: String, resultLimit: Int, matchedItemHandler: ([Any]) -> Void)](nsuserinterfaceitemsearching/searchforitems(withsearch:resultlimit:matcheditemhandler:).md)
  Search for the specified items, with the result limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/performaction(foritem:))*