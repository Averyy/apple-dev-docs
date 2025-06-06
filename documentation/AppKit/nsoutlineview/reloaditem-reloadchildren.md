# reloadItem(_:reloadChildren:)

**Framework**: AppKit  
**Kind**: method

Reloads a given item and, optionally, its children.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadItem(_ item: Any?, reloadChildren: Bool)
```

## Parameters

- `item`: Starting in OS X version 10.5,  passing   will reload everything under the root in the outline view.
- `reloadChildren`: It is not necessary, or efficient, to reload children if the item is not expanded.

## See Also

- [func reloadItem(Any?)](nsoutlineview/reloaditem(_:).md)
  Reloads and redisplays the data for the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/reloaditem(_:reloadchildren:))*