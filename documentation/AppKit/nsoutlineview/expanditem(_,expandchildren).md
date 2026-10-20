# expandItem(_:expandChildren:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Expands a specified item and, optionally, its children.

**Availability**:
- macOS

## Declaration

```swift
func expandItem(_ item: Any?, expandChildren: Bool)
```

```objc
- (void) expandItem:(id) item expandChildren:(BOOL) expandChildren;
```

#### Discussion

For example, this method is invoked with the `expandChildren` parameter set to [`true`](../../Swift/true.md) when a user Option-clicks the disclosure triangle for an item in the outline view (to expand the item and all its contained items).

For each item expanded, posts an item expanded notification.

## Parameters

- `item`: An item in the receiver.

  Starting in OS X version 10.5,  passing `'nil'` will expand each item under the root in the outline view.
- `expandChildren`: If [`true`](../../Swift/true.md), recursively expands `item` and its children. If [`false`](../../Swift/false.md), expands `item` only (identical to [`expandItem(_:)`](./expanditem%28_%29.md)).

## See Also

### Expanding and Collapsing the Outline
- [func expandItem(Any?)](./expanditem%28_%29.md)
  Expands a given item.
- [func collapseItem(Any?)](./collapseitem%28_%29.md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](./collapseitem%28_,collapsechildren%29.md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/expanditem(_:expandchildren:))*