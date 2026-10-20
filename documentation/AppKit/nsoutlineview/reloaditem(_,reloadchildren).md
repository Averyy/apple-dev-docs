# reloadItem(_:reloadChildren:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reloads a given item and, optionally, its children.

**Availability**:
- macOS

## Declaration

```swift
func reloadItem(_ item: Any?, reloadChildren: Bool)
```

```objc
- (void) reloadItem:(id) item reloadChildren:(BOOL) reloadChildren;
```

## Parameters

- `item`: An item in the receiver.

  Starting in OS X version 10.5,  passing `'nil'` will reload everything under the root in the outline view.
- `reloadChildren`: If [`true`](../../Swift/true.md), recursively reloads `item` and its children. If [`false`](../../Swift/false.md), reloads `item` only (identical to [`reloadItem(_:)`](./reloaditem%28_%29.md)).

  It is not necessary, or efficient, to reload children if the item is not expanded.

## See Also

### Redisplaying Information
- [func reloadItem(Any?)](./reloaditem%28_%29.md)
  Reloads and redisplays the data for the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/reloaditem(_:reloadchildren:))*