# collectionView(_:layout:sizeForItemAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the size of the specified item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, layout collectionViewLayout: NSCollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> NSSize
```

#### Return Value

The size of the item. The width and height values must both be greater than `0`. Items must also not exceed the available space in the collection view.

#### Discussion

Implement this method when you want to provide the size of items in the flow layout. Your implementation can return the same size for all items or it can return different sizes for items. You can also adjust the size of items dynamically each time you update the layout. If you do not implement this method, the size of items is obtained from the properties of the flow layout object.

The size value you return from this method must allow the item to be displayed fully by the collection view. In the scrolling direction, items can be larger than the collection view because the remaining content can always be scrolled into view, but in the nonscrolling directions, items should always be smaller than the collection view itself. For example, the width of an item in a vertically scrolling collection view must not exceed the width of the collection view minus any section insets. The flow layout does not crop an item’s bounds to make it fit into the available space.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `indexPath`: The index path of the item.

## See Also

- [var estimatedItemSize: NSSize](nscollectionviewflowlayout/estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegateflowlayout/collectionview(_:layout:sizeforitemat:))*