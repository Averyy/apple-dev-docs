# parent(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the parent for a given item.

**Availability**:
- macOS

## Declaration

```swift
func parent(forItem item: Any?) -> Any?
```

```objc
- (id) parentForItem:(id) item;
```

## Return Value

The parent for `item`, or `nil` if the parent is the root.

## Parameters

- `item`: The item for which to return the parent.

## See Also

### Getting Related Items
- [func childIndex(forItem: Any) -> Int](./childindex%28foritem%29.md)
  Returns the child index of the specified item within its parent.
- [func child(Int, ofItem: Any?) -> Any?](./child%28_,ofitem%29.md)
  Returns the specified child of an item.
- [func numberOfChildren(ofItem: Any?) -> Int](./numberofchildren%28ofitem%29.md)
  Returns the number of children for the specified parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/parent(foritem:))*