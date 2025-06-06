# expandItem(_:expandChildren:)

**Framework**: AppKit  
**Kind**: method

Expands a specified item and, optionally, its children.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func expandItem(_ item: Any?, expandChildren: Bool)
```

#### Discussion

For example, this method is invoked with the `expandChildren` parameter set to [`true`](https://developer.apple.com/documentation/swift/true) when a user Option-clicks the disclosure triangle for an item in the outline view (to expand the item and all its contained items).

For each item expanded, posts an item expanded notification.

## Parameters

- `item`: Starting in OS X version 10.5,  passing   will expand each item under the root in the outline view.
- `expandChildren`: If  , recursively expands   and its children. If  , expands   only (identical to  ).

## See Also

- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func collapseItem(Any?)](nsoutlineview/collapseitem(_:).md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](nsoutlineview/collapseitem(_:collapsechildren:).md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/expanditem(_:expandchildren:))*