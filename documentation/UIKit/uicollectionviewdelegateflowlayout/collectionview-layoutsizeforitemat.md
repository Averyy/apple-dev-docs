# collectionView(_:layout:sizeForItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the size of the specified item’s cell.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize
```

#### Return Value

The width and height of the specified item. Both values must be greater than 0.

#### Discussion

If you do not implement this method, the flow layout uses the values in its [`itemSize`](uicollectionviewflowlayout/itemsize.md) property to set the size of items instead. Your implementation of this method can return a fixed set of sizes or dynamically adjust the sizes based on the cell’s content.

The flow layout does not crop a cell’s bounds to make it fit into the grid. Therefore, the values you return must allow for the item to be displayed fully in the collection view. For example, in a vertically scrolling grid, the width of a single item must not exceed the width of the collection view (minus any section insets) itself. However, in the scrolling direction, items can be larger than the collection view because the remaining content can always be scrolled into view.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `indexPath`: The index path of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:sizeforitemat:))*