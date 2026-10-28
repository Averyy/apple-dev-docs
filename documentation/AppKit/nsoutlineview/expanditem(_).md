# expandItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Expands a given item.

**Availability**:
- macOS

## Declaration

```swift
func expandItem(_ item: Any?)
```

```objc
- (void) expandItem:(id) item;
```

## Discussion

If `item` is not expandable or is already expanded, does nothing.

If expanding takes place, posts an item expanded notification.

## Parameters

- `item`: An item in the receiver.

## See Also

### Expanding and Collapsing the Outline
- [func expandItem(Any?, expandChildren: Bool)](./expanditem%28_,expandchildren%29.md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?)](./collapseitem%28_%29.md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](./collapseitem%28_,collapsechildren%29.md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/expanditem(_:))*