# collectionView(_:didEndDisplaying:forRepresentedObjectAt:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that the specified item was removed from the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, didEndDisplaying item: NSCollectionViewItem, forRepresentedObjectAt indexPath: IndexPath)
```

#### Discussion

The collection view calls this method after removing an item from its content. You can use this method to track the removal of items and perform related tasks.

## Parameters

- `collectionView`: The collection view that removed the item.
- `item`: The item that was removed.
- `indexPath`: The index path of the item.

## See Also

- [func collectionView(NSCollectionView, willDisplay: NSCollectionViewItem, forRepresentedObjectAt: IndexPath)](nscollectionviewdelegate/collectionview(_:willdisplay:forrepresentedobjectat:).md)
  Notifies the delegate that the specified item is about to be displayed by the collection view.
- [func collectionView(NSCollectionView, willDisplaySupplementaryView: NSView, forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath)](nscollectionviewdelegate/collectionview(_:willdisplaysupplementaryview:forelementkind:at:).md)
  Notifies the delegate that the specified supplementary view is about to be displayed by the collection view.
- [func collectionView(NSCollectionView, didEndDisplayingSupplementaryView: NSView, forElementOfKind: NSCollectionView.SupplementaryElementKind, at: IndexPath)](nscollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:).md)
  Notifies the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:didenddisplaying:forrepresentedobjectat:))*