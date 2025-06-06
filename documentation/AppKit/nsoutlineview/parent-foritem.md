# parent(forItem:)

**Framework**: AppKit  
**Kind**: method

Returns the parent for a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func parent(forItem item: Any?) -> Any?
```

#### Return Value

The parent for `item`, or `nil` if the parent is the root.

## Parameters

- `item`: The item for which to return the parent.

## See Also

- [func childIndex(forItem: Any) -> Int](nsoutlineview/childindex(foritem:).md)
  Returns the child index of the specified item within its parent.
- [func child(Int, ofItem: Any?) -> Any?](nsoutlineview/child(_:ofitem:).md)
  Returns the specified child of an item.
- [func numberOfChildren(ofItem: Any?) -> Int](nsoutlineview/numberofchildren(ofitem:).md)
  Returns the number of children for the specified parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/parent(foritem:))*