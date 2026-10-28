# numberOfChildren(ofItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of children for the specified parent item.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func numberOfChildren(ofItem item: Any?) -> Int
```

```objc
- (NSInteger) numberOfChildrenOfItem:(id) item;
```

## Return Value

The number of children associated with the parent.

## Discussion

You can call this method on an outline view with either a static or dynamic data source. For an outline view whose contents are dynamic, this method may call out to the [`outlineView(_:numberOfChildrenOfItem:)`](../nsoutlineviewdatasource/outlineview%28_,numberofchildrenofitem%29.md) method of the associated data source object.

## Parameters

- `item`: The parent item.

## See Also

### Getting Related Items
- [func parent(forItem: Any?) -> Any?](./parent%28foritem%29.md)
  Returns the parent for a given item.
- [func childIndex(forItem: Any) -> Int](./childindex%28foritem%29.md)
  Returns the child index of the specified item within its parent.
- [func child(Int, ofItem: Any?) -> Any?](./child%28_,ofitem%29.md)
  Returns the specified child of an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/numberofchildren(ofitem:))*