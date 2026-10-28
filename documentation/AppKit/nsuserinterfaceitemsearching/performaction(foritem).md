# performAction(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the user selects a search result in Help menu.

**Availability**:
- macOS

## Declaration

```swift
optional func performAction(forItem item: Any)
```

```objc
- (void) performActionForItem:(id) item;
```

## Discussion

The default implementation brings up Help Viewer for a Help item.

## Parameters

- `item`: An item in the help menu.

## See Also

### Search Help Content
- [func searchForItems(withSearch: String, resultLimit: Int, matchedItemHandler: ([Any]) -> Void)](./searchforitems%28withsearch,resultlimit,matcheditemhandler%29.md)
  Search for the specified items, with the result limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/performaction(foritem:))*