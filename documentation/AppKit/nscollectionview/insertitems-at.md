# insertItems(at:)

**Framework**: AppKit  
**Kind**: method

Inserts new items into the collection view at the specified locations.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func insertItems(at indexPaths: Set<IndexPath>)
```

#### Discussion

After adding new items to your data source object, use this method to synchronize those changes with the collection view. Calling this method lets the collection view know that it must update its internal data structures and possibly update its visual appearance. In response, the collection view asks the layout object for information about the new objects. If the layout object indicates that the new items should appear onscreen, the collection view asks the data source to provide the appropriate content, animating that content into position as needed.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `indexPaths`: A set of   objects, each of which includes a section and item index corresponding to the insertion point of a single item. Specifying   for this parameter raises an exception.

## See Also

- [func moveItem(at: IndexPath, to: IndexPath)](nscollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.
- [func deleteItems(at: Set<IndexPath>)](nscollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/insertitems(at:))*