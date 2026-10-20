# reconfigureItems(withIdentifiers:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reconfigureItems(withIdentifiers identifiers: [Any])
```

```objc
- (void) reconfigureItemsWithIdentifiers:(NSArray<id> *) identifiers;
```

#### Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [`reloadItems(withIdentifiers:)`](./reloaditems%28withidentifiers%29.md). For optimal performance, choose to reconfigure items instead of reloading items unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the collection view or table view doesn’t call `prepareForReuse` for each cell dequeued. If you need to return a different type of cell for an index path, use [`reloadItems(withIdentifiers:)`](./reloaditems%28withidentifiers%29.md) instead.

If your cells are self-sizing, the collection view or table view resizes your cells after reconfiguring them.

Set the `animatingDifferences` parameter to tell the collection view or table view whether to animate any size or layout changes that are a result of reconfiguration when you apply the snapshot to your data source. To avoid animations when setting specific properties, use [`performWithoutAnimation(_:)`](../uiview/performwithoutanimation%28_%29.md) in your cell configuration logic.

If your collection view or table view uses a diffable data source, use this method. If your collection view uses a custom implementation of `UICollectionViewDataSource`, use [`reconfigureItems(at:)`](../uicollectionview/reconfigureitems%28at%29.md) instead. If your table view uses a custom implementation of `UITableViewDataSource`, use [`reconfigureRows(at:)`](../uitableview/reconfigurerows%28at%29.md) instead.

## Parameters

- `identifiers`: An array of identifiers corresponding to the items to update data for in the snapshot.

## See Also

### Reloading data
- [var reconfiguredItemIdentifiers: [Any]](./reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems(withIdentifiers: [Any])](./reloaditems%28withidentifiers%29.md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [Any]](./reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections(withIdentifiers: [Any])](./reloadsections%28withidentifiers%29.md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [Any]](./reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:))*