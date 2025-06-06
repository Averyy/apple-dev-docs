# moveItem(at:to:)

**Framework**: UIKit  
**Kind**: method

Moves an item from one location to another in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func moveItem(at indexPath: IndexPath, to newIndexPath: IndexPath)
```

#### Discussion

Use this method to reorganize existing data items. You might do this when you rearrange the items within your data source object or in response to user interactions with the collection view. You can move items between sections or within the same section. The collection view updates the layout as needed to account for the move, animating cells into position as needed.

You can also call this method from a block passed to the [`performBatchUpdates(_:completion:)`](uicollectionview/performbatchupdates(_:completion:).md) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## Parameters

- `indexPath`: The index path of the item you want to move. This parameter must not be  .
- `newIndexPath`: The index path of the item’s new location. This parameter must not be  .

## See Also

- [func insertItems(at: [IndexPath])](uicollectionview/insertitems(at:).md)
  Inserts new items at the specified index paths.
- [func deleteItems(at: [IndexPath])](uicollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/moveitem(at:to:))*