# reloadItem(_:reloadChildren:)

**Framework**: AppKit  
**Kind**: method

Reloads a given item and, optionally, its children.

**Availability**:
- macOS ?+

## Declaration

```swift
func reloadItem(_ item: Any?, reloadChildren: Bool)
```

## Parameters

- `item`: An item in the receiver. Starting in OS X version 10.5,  passing `'nil'` will reload everything under the root in the outline view.
- `reloadChildren`: If [`true`](https://developer.apple.com/documentation/Swift/true), recursively reloads `item` and its children. If [`false`](https://developer.apple.com/documentation/Swift/false), reloads `item` only (identical to [`reloadItem(_:)`](nsoutlineview/reloaditem(_:).md)). It is not necessary, or efficient, to reload children if the item is not expanded.

## See Also

- [func reloadItem(Any?)](nsoutlineview/reloaditem(_:).md)
  Reloads and redisplays the data for the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/reloaditem(_:reloadchildren:))*