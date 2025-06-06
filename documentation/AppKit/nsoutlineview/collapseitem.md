# collapseItem(_:)

**Framework**: AppKit  
**Kind**: method

Collapses a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func collapseItem(_ item: Any?)
```

#### Discussion

If `item` is not expanded or not expandable, does nothing

If collapsing takes place, posts item collapse notification.

## Parameters

- `item`: An item in the receiver.

## See Also

- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func expandItem(Any?, expandChildren: Bool)](nsoutlineview/expanditem(_:expandchildren:).md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?, collapseChildren: Bool)](nsoutlineview/collapseitem(_:collapsechildren:).md)
  Collapses a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/collapseitem(_:))*