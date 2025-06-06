# child(_:ofItem:)

**Framework**: AppKit  
**Kind**: method

Returns the specified child of an item.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func child(_ index: Int, ofItem item: Any?) -> Any?
```

#### Return Value

The child item or `nil` if the item could not be found.

#### Discussion

You can call this method on an outline view with either a static or dynamic data source. For an outline view whose contents are dynamic, this method may call out to the [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md) method of the associated data source object.

## Parameters

- `index`: The index of the child item in the parent.
- `item`: The parent item whose child item you want to retrieve.

## See Also

- [func parent(forItem: Any?) -> Any?](nsoutlineview/parent(foritem:).md)
  Returns the parent for a given item.
- [func childIndex(forItem: Any) -> Int](nsoutlineview/childindex(foritem:).md)
  Returns the child index of the specified item within its parent.
- [func numberOfChildren(ofItem: Any?) -> Int](nsoutlineview/numberofchildren(ofitem:).md)
  Returns the number of children for the specified parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/child(_:ofitem:))*