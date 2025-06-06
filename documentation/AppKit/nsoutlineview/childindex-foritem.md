# childIndex(forItem:)

**Framework**: AppKit  
**Kind**: method

Returns the child index of the specified item within its parent.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func childIndex(forItem item: Any) -> Int
```

#### Discussion

The performance of this method is O(1) at best and O(n) at worst.

## See Also

- [func parent(forItem: Any?) -> Any?](nsoutlineview/parent(foritem:).md)
  Returns the parent for a given item.
- [func child(Int, ofItem: Any?) -> Any?](nsoutlineview/child(_:ofitem:).md)
  Returns the specified child of an item.
- [func numberOfChildren(ofItem: Any?) -> Int](nsoutlineview/numberofchildren(ofitem:).md)
  Returns the number of children for the specified parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/childindex(foritem:))*