# collapseItem(_:collapseChildren:)

**Framework**: AppKit  
**Kind**: method

Collapses a given item and, optionally, its children.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func collapseItem(_ item: Any?, collapseChildren: Bool)
```

#### Discussion

For example, this method is invoked with the `collapseChildren` parameter set to [`true`](https://developer.apple.com/documentation/swift/true) when a user Option-clicks the disclosure triangle for an item in the outline view (to collapse the item and all its contained items).

For each item collapsed, posts an item collapsed notification.

## Parameters

- `item`: Starting in OS X version 10.5,  passing   will collapse each item under the root in the outline view.
- `collapseChildren`: If  , recursively collapses   and its children. If  , collapses   only (identical to  ).

## See Also

- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func expandItem(Any?, expandChildren: Bool)](nsoutlineview/expanditem(_:expandchildren:).md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?)](nsoutlineview/collapseitem(_:).md)
  Collapses a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/collapseitem(_:collapsechildren:))*