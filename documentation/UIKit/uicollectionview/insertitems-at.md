# insertItems(at:)

**Framework**: UIKit  
**Kind**: method

Inserts new items at the specified index paths.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertItems(at indexPaths: [IndexPath])
```

#### Discussion

Call this method to insert one or more new items into the collection view. You might do this when your data source object receives data for new items or in response to user interactions with the collection view. The collection view gets the layout information for the new cells as part of calling this method. And if the layout information indicates that the cells should appear onscreen, the collection view asks your data source to provide the appropriate views, animating them into position as needed.

You can also call this method from a block passed to the [`performBatchUpdates(_:completion:)`](uicollectionview/performbatchupdates(_:completion:).md) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## Parameters

- `indexPaths`: An array of   objects, each of which contains a section index and item index at which to insert a new cell. This parameter must not be  .

## See Also

- [func moveItem(at: IndexPath, to: IndexPath)](uicollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.
- [func deleteItems(at: [IndexPath])](uicollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/insertitems(at:))*