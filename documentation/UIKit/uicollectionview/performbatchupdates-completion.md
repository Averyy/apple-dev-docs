# performBatchUpdates(_:completion:)

**Framework**: UIKit  
**Kind**: method

Animates multiple insert, delete, reload, and move operations as a group.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performBatchUpdates(_ updates: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

#### Discussion

You can use this method in cases where you want to make multiple changes to the collection view in one single animated operation, as opposed to in several separate animations. You might use this method to insert, delete, reload, or move cells or use it to change the layout parameters associated with one or more cells. Use the block passed in the `updates` parameter to specify all of the operations you want to perform.

If the collection view’s layout isn’t up to date before you call this method, a reload may occur. To avoid problems, you should update your data model inside the `updates` block or ensure the layout is updated before you call [`performBatchUpdates(_:completion:)`](uicollectionview/performbatchupdates(_:completion:).md).

Deletes are processed before inserts in batch operations. This means the indexes for the deletions are processed relative to the indexes of the collection view’s state before the batch operation, and the indexes for the insertions are processed relative to the indexes of the state after all the deletions in the batch operation.

## Parameters

- `updates`: The block that performs the relevant insert, delete, reload, or move operations.
- `completion`: A completion handler block to execute when all of the operations finish. This block takes a single Boolean parameter that contains the value   if all of the related animations completed successfully or   if they were interrupted. This parameter may be  .

## See Also

- [func deleteItems(at: [IndexPath])](uicollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.
- [func moveSection(Int, toSection: Int)](uicollectionview/movesection(_:tosection:).md)
  Moves a section from one location to another in the collection view.
- [func moveItem(at: IndexPath, to: IndexPath)](uicollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.
- [func insertItems(at: [IndexPath])](uicollectionview/insertitems(at:).md)
  Inserts new items at the specified index paths.
- [func insertSections(IndexSet)](uicollectionview/insertsections(_:).md)
  Inserts new sections at the specified indexes.
- [func deleteSections(IndexSet)](uicollectionview/deletesections(_:).md)
  Deletes the sections at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/performbatchupdates(_:completion:))*