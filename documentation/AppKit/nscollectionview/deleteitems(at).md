# deleteItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deletes the items at the specified index paths.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func deleteItems(at indexPaths: Set<IndexPath>)
```

```objc
- (void) deleteItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths;
```

## Discussion

After removing items from your data source object, use this method to synchronize those changes with the collection view. Calling this method lets the collection view know that it must update its internal data structures and possibly update its visual appearance. In response, the collection view asks the layout object to update the positions of the remaining objects. If the layout object indicates that there are changes to the visible items, the collection view animates the affected items into place.

When inserting or deleting multiple sections and items, you can animate all of your changes at once using the [`performBatchUpdates(_:completionHandler:)`](./performbatchupdates%28_,completionhandler%29.md) method.

## Parameters

- `indexPaths`: A set of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects, each of which includes a section and item index corresponding to the insertion point of a single item. Specifying `nil` for this parameter raises an exception.

## See Also

### Inserting, Moving, and Deleting Items
- [func insertItems(at: Set<IndexPath>)](./insertitems%28at%29.md)
  Inserts new items into the collection view at the specified locations.
- [func moveItem(at: IndexPath, to: IndexPath)](./moveitem%28at,to%29.md)
  Moves an item from one location to another in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deleteitems(at:))*