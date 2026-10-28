# isExpandable(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a given item is expandable.

**Availability**:
- macOS

## Declaration

```swift
func isExpandable(_ item: Any?) -> Bool
```

```objc
- (BOOL) isExpandable:(id) item;
```

## Return Value

[`true`](../../Swift/true.md) if `item` is expandable—that is, `item` can contain other items, otherwise [`false`](../../Swift/false.md).

## Parameters

- `item`: An item in the receiver.

## See Also

### Related Documentation
- [func expandItem(Any?)](./expanditem%28_%29.md)
  Expands a given item.
### Working with Expandability
- [func isItemExpanded(Any?) -> Bool](./isitemexpanded%28_%29.md)
  Returns a Boolean value that indicates whether a given item is expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/isexpandable(_:))*