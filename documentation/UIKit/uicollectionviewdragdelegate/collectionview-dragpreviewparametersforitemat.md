# collectionView(_:dragPreviewParametersForItemAt:)

**Framework**: UIKit  
**Kind**: method

Returns custom information about how to display the item at the specified location during the drag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, dragPreviewParametersForItemAt indexPath: IndexPath) -> UIDragPreviewParameters?
```

#### Return Value

Drag parameters that indicate how to display the cell’s content during a drag.

#### Discussion

Use this method to customize the appearance of the item during drags. If you don’t implement this method or if you implement it and return `nil`, the collection view uses the cell’s visible bounds to create the preview.

In your implementation, create a [`UIDragPreviewParameters`](uidragpreviewparameters.md) object and update the preview information for the specified item. Use the parameters to specify the portion of the cell that you want to be included in the drag preview or to change the background color drawn beneath your cell.

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `indexPath`: The index path of the item being dragged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragpreviewparametersforitemat:))*