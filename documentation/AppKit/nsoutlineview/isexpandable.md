# isExpandable(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether a given item is expandable.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isExpandable(_ item: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `item` is expandable—that is, `item` can contain other items, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `item`: An item in the receiver.

## See Also

- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func isItemExpanded(Any?) -> Bool](nsoutlineview/isitemexpanded(_:).md)
  Returns a Boolean value that indicates whether a given item is expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/isexpandable(_:))*