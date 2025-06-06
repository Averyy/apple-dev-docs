# deleteItems(at:)

**Framework**: AppKit  
**Kind**: method

Deletes the items at the specified index paths.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func deleteItems(at indexPaths: Set<IndexPath>)
```

#### Discussion

After removing items from your data source object, use this method to synchronize those changes with the collection view. Calling this method lets the collection view know that it must update its internal data structures and possibly update its visual appearance. In response, the collection view asks the layout object to update the positions of the remaining objects. If the layout object indicates that there are changes to the visible items, the collection view animates the affected items into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `indexPaths`: A set of   objects, each of which includes a section and item index corresponding to the insertion point of a single item. Specifying   for this parameter raises an exception.

## See Also

- [func insertItems(at: Set<IndexPath>)](nscollectionview/insertitems(at:).md)
  Inserts new items into the collection view at the specified locations.
- [func moveItem(at: IndexPath, to: IndexPath)](nscollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deleteitems(at:))*