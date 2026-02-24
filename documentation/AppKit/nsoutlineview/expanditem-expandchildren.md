# expandItem(_:expandChildren:)

**Framework**: AppKit  
**Kind**: method

Expands a specified item and, optionally, its children.

**Availability**:
- macOS ?+

## Declaration

```swift
func expandItem(_ item: Any?, expandChildren: Bool)
```

#### Discussion

For example, this method is invoked with the `expandChildren` parameter set to [`true`](https://developer.apple.com/documentation/Swift/true) when a user Option-clicks the disclosure triangle for an item in the outline view (to expand the item and all its contained items).

For each item expanded, posts an item expanded notification.

## Parameters

- `item`: An item in the receiver. Starting in OS X version 10.5,  passing `'nil'` will expand each item under the root in the outline view.
- `expandChildren`: If [`true`](https://developer.apple.com/documentation/Swift/true), recursively expands `item` and its children. If [`false`](https://developer.apple.com/documentation/Swift/false), expands `item` only (identical to [`expandItem(_:)`](nsoutlineview/expanditem(_:).md)).

## See Also

- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func collapseItem(Any?)](nsoutlineview/collapseitem(_:).md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](nsoutlineview/collapseitem(_:collapsechildren:).md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/expanditem(_:expandchildren:))*