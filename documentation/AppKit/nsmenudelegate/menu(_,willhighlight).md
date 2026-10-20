# menu(_:willHighlight:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to indicate that a menu is about to highlight a given item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func menu(_ menu: NSMenu, willHighlight item: NSMenuItem?)
```

```objc
- (void) menu:(NSMenu *) menu willHighlightItem:(NSMenuItem *) item;
```

#### Discussion

Only one item per menu can be highlighted at a time. If `item` is `nil`, it means that all items in the menu are about to be unhighlighted.

## Parameters

- `menu`: The menu object about to highlight an item.
- `item`: The item about to be highlighted.

## See Also

### Related Documentation
- [var highlightedItem: NSMenuItem?](../nsmenu/highlighteditem.md)
  Indicates the currently highlighted item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menu(_:willhighlight:))*