# expandItem(_:)

**Framework**: AppKit  
**Kind**: method

Expands a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func expandItem(_ item: Any?)
```

#### Discussion

If `item` is not expandable or is already expanded, does nothing.

If expanding takes place, posts an item expanded notification.

## Parameters

- `item`: An item in the receiver.

## See Also

- [func expandItem(Any?, expandChildren: Bool)](nsoutlineview/expanditem(_:expandchildren:).md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?)](nsoutlineview/collapseitem(_:).md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](nsoutlineview/collapseitem(_:collapsechildren:).md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/expanditem(_:))*