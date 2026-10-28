# collapseItem(_:collapseChildren:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Collapses a given item and, optionally, its children.

**Availability**:
- macOS

## Declaration

```swift
func collapseItem(_ item: Any?, collapseChildren: Bool)
```

```objc
- (void) collapseItem:(id) item collapseChildren:(BOOL) collapseChildren;
```

## Discussion

For example, this method is invoked with the `collapseChildren` parameter set to [`true`](../../Swift/true.md) when a user Option-clicks the disclosure triangle for an item in the outline view (to collapse the item and all its contained items).

For each item collapsed, posts an item collapsed notification.

## Parameters

- `item`: An item in the receiver.

  Starting in OS X version 10.5,  passing `'nil'` will collapse each item under the root in the outline view.
- `collapseChildren`: If [`true`](../../Swift/true.md), recursively collapses `item` and its children. If [`false`](../../Swift/false.md), collapses `item` only (identical to [`collapseItem(_:)`](./collapseitem%28_%29.md)).

## See Also

### Expanding and Collapsing the Outline
- [func expandItem(Any?)](./expanditem%28_%29.md)
  Expands a given item.
- [func expandItem(Any?, expandChildren: Bool)](./expanditem%28_,expandchildren%29.md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?)](./collapseitem%28_%29.md)
  Collapses a given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/collapseitem(_:collapsechildren:))*