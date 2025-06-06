# moveItem(at:to:)

**Framework**: AppKit  
**Kind**: method

Moves an item from one location to another in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func moveItem(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

#### Discussion

After rearranging items in your data source object, use this method to synchronize those changes with the collection view. Calling this method lets the collection view know that it must update its internal data structures and possibly update its visual appearance. You can move the item to a different section or to a new location in the same section. The collection view updates the layout as needed to account for the move, animating cells into position in response.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](nscollectionview/performbatchupdates(_:completionhandler:).md) method.

## Parameters

- `indexPath`: The index path of the item that you want to move. This parameter must not be  .
- `newIndexPath`: The index path of the item’s new location. This parameter must not be  .

## See Also

- [func insertItems(at: Set<IndexPath>)](nscollectionview/insertitems(at:).md)
  Inserts new items into the collection view at the specified locations.
- [func deleteItems(at: Set<IndexPath>)](nscollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/moveitem(at:to:))*