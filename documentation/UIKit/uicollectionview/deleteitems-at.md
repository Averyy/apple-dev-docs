# deleteItems(at:)

**Framework**: UIKit  
**Kind**: method

Deletes the items at the specified index paths.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func deleteItems(at indexPaths: [IndexPath])
```

#### Discussion

Use this method to remove items from the collection view. You might do this when you remove the items from your data source object or in response to user interactions with the collection view. The collection view updates the layout of the remaining items to account for the deletions, animating the remaining items into position as needed.

You can also call this method from a block passed to the [`performBatchUpdates(_:completion:)`](uicollectionview/performbatchupdates(_:completion:).md) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## Parameters

- `indexPaths`: An array of   objects, each of which contains a section index and item index for the item you want to delete from the collection view. This parameter must not be  .

## See Also

- [func insertItems(at: [IndexPath])](uicollectionview/insertitems(at:).md)
  Inserts new items at the specified index paths.
- [func moveItem(at: IndexPath, to: IndexPath)](uicollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/deleteitems(at:))*