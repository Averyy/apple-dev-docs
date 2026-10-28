# setDropItem(_:dropChildIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used to “retarget” a proposed drop.

**Availability**:
- macOS

## Declaration

```swift
func setDropItem(_ item: Any?, dropChildIndex index: Int)
```

```objc
- (void) setDropItem:(id) item dropChildIndex:(NSInteger) index;
```

## Discussion

For example, to specify a drop on `someOutlineItem`, you specify `item` as `someOutlineItem` and `index` as [`NSOutlineViewDropOnItemIndex`](../nsoutlineviewdroponitemindex.md). To specify a drop between child `2` and `3` of `someOutlineItem`, you specify `item` as `someOutlineItem` and `index` as `3` (children are a zero-based index). To specify a drop on an un-expandable `someOutlineItem`, you specify `item` as `someOutlineItem` and `index` as [`NSOutlineViewDropOnItemIndex`](../nsoutlineviewdroponitemindex.md).

## Parameters

- `item`: The target item.
- `index`: The drop index.

## See Also

### Supporting Drag and Drop
- [func shouldCollapseAutoExpandedItems(forDeposited: Bool) -> Bool](./shouldcollapseautoexpandeditems%28fordeposited%29.md)
  Returns a Boolean value that indicates whether auto-expanded items should return to their original collapsed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/setdropitem(_:dropchildindex:))*