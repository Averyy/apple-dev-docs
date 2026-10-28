# childIndex(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the child index of the specified item within its parent.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func childIndex(forItem item: Any) -> Int
```

```objc
- (NSInteger) childIndexForItem:(id) item;
```

## Discussion

The performance of this method is O(1) at best and O(n) at worst.

## See Also

### Getting Related Items
- [func parent(forItem: Any?) -> Any?](./parent%28foritem%29.md)
  Returns the parent for a given item.
- [func child(Int, ofItem: Any?) -> Any?](./child%28_,ofitem%29.md)
  Returns the specified child of an item.
- [func numberOfChildren(ofItem: Any?) -> Int](./numberofchildren%28ofitem%29.md)
  Returns the number of children for the specified parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/childindex(foritem:))*