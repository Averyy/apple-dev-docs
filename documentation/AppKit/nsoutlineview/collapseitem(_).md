# collapseItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Collapses a given item.

**Availability**:
- macOS

## Declaration

```swift
func collapseItem(_ item: Any?)
```

```objc
- (void) collapseItem:(id) item;
```

#### Discussion

If `item` is not expanded or not expandable, does nothing

If collapsing takes place, posts item collapse notification.

## Parameters

- `item`: An item in the receiver.

## See Also

### Expanding and Collapsing the Outline
- [func expandItem(Any?)](./expanditem%28_%29.md)
  Expands a given item.
- [func expandItem(Any?, expandChildren: Bool)](./expanditem%28_,expandchildren%29.md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?, collapseChildren: Bool)](./collapseitem%28_,collapsechildren%29.md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/collapseitem(_:))*