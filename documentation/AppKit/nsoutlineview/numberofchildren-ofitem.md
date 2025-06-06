# numberOfChildren(ofItem:)

**Framework**: AppKit  
**Kind**: method

Returns the number of children for the specified parent item.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func numberOfChildren(ofItem item: Any?) -> Int
```

#### Return Value

The number of children associated with the parent.

#### Discussion

You can call this method on an outline view with either a static or dynamic data source. For an outline view whose contents are dynamic, this method may call out to the [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md) method of the associated data source object.

## Parameters

- `item`: The parent item.

## See Also

- [func parent(forItem: Any?) -> Any?](nsoutlineview/parent(foritem:).md)
  Returns the parent for a given item.
- [func childIndex(forItem: Any) -> Int](nsoutlineview/childindex(foritem:).md)
  Returns the child index of the specified item within its parent.
- [func child(Int, ofItem: Any?) -> Any?](nsoutlineview/child(_:ofitem:).md)
  Returns the specified child of an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/numberofchildren(ofitem:))*