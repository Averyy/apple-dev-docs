# drop(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Animates the item to the specified location and inserts a placeholder cell at that location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drop(_ dragItem: UIDragItem, to placeholder: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Return Value

The context object that you use to replace or remove the placeholder cell later. Store a reference to this object so that you can call its methods later.

#### Discussion

Use this method to insert a temporary placeholder cell (instead of a cell backed by actual data) into the collection view. When calling this method, don’t update your data source object to account for the placeholder. The collection view manages the placeholder until you explicitly remove it using the returned context object.

Typically, you use this method when you must load data asynchronously for a cell. Instead of updating your data source, you insert a placeholder cell. When the data is finally available, update your data source object and call the [`commitInsertion(dataSourceUpdates:)`](uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md) method of the returned context object to swap out the placeholder cell for an actual cell. You can also remove a placeholder cell that’s no longer needed by calling the [`deletePlaceholder()`](uicollectionviewdropplaceholdercontext/deleteplaceholder().md) method.

At some point after calling this method, the collection view executes your `cellUpdateHandler` block. Use that block to configure the contents of the placeholder cell. Calling the [`setNeedsCellUpdate()`](uicollectionviewdropplaceholdercontext/setneedscellupdate().md) method of the returned context object executes your handler again, giving you a way to update the cell later.

## Parameters

- `dragItem`: The drag item containing the data to drop.
- `placeholder`: The placeholder to add at the specified location.

## See Also

- [func drop(UIDragItem, toItemAt: IndexPath) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:toitemat:).md)
  Animates the item to the specified index path in the collection view.
- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:intoitemat:rect:).md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:to:)-7w5rn.md)
  Animates the item to an arbitrary location in your view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-l5tg)*