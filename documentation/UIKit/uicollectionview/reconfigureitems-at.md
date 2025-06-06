# reconfigureItems(at:)

**Framework**: UIKit  
**Kind**: method

Updates the data for the items at the index paths you specify, preserving the existing cells for the items.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reconfigureItems(at indexPaths: [IndexPath])
```

#### Discussion

To update the contents of existing (including prefetched) cells without replacing them with new cells, use this method instead of [`reloadItems(at:)`](uicollectionview/reloaditems(at:).md). For optimal performance, choose to reconfigure items instead of reloading items unless you have an explicit need to replace the existing cell with a new cell.

Your cell provider must dequeue the same type of cell for the provided index path, and must return the same existing cell for a given index path. Because this method reconfigures existing cells, the collection view doesn’t call [`prepareForReuse()`](uicollectionreusableview/prepareforreuse().md) for each cell dequeued. If you need to return a different type of cell for an index path, use [`reloadItems(at:)`](uicollectionview/reloaditems(at:).md) instead.

If your cells are self-sizing, the collection view resizes your cells after reconfiguring them.

By default, the collection view animates any size or layout changes that result from reconfiguration. To reconfigure cells without animation, use `UIView`’s [`performWithoutAnimation(_:)`](uiview/performwithoutanimation(_:).md) when you call this method. Alternatively, to avoid animations when setting specific properties, use [`performWithoutAnimation(_:)`](uiview/performwithoutanimation(_:).md) in your cell configuration logic.

If your collection view uses a custom implementation of `UICollectionViewDataSource`, use this method. If your collection view uses a diffable data source, use [`reconfigureItems(_:)`](nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:).md) (Swift) or [`reconfigureItems(withIdentifiers:)`](nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:).md) (Objective-C) on `NSDiffableDataSourceSnapshot` instead.

## Parameters

- `indexPaths`: An array of   objects identifying the items you want to update.

## See Also

- [var hasUncommittedUpdates: Bool](uicollectionview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reloadData()](uicollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](uicollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.
- [func reloadItems(at: [IndexPath])](uicollectionview/reloaditems(at:).md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems(at:))*