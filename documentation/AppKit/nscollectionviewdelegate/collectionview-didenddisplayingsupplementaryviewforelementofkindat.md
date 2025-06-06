# collectionView(_:didEndDisplayingSupplementaryView:forElementOfKind:at:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that the specified supplementary view was removed from the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, didEndDisplayingSupplementaryView view: NSView, forElementOfKind elementKind: NSCollectionView.SupplementaryElementKind, at indexPath: IndexPath)
```

#### Discussion

The collection view calls this method after removing a supplementary view from its content. You can use this method to track the removal of views and perform related tasks.

## Parameters

- `collectionView`: The collection view that removed the view.
- `view`: The supplementary view that was removed.
- `elementKind`: The type of the supplementary view. Layouts are responsible for defining the types of supplementary views they support.
- `indexPath`: The index path associated with the supplementary view.

## See Also

- [func collectionView(NSCollectionView, willDisplay: NSCollectionViewItem, forRepresentedObjectAt: IndexPath)](nscollectionviewdelegate/collectionview(_:willdisplay:forrepresentedobjectat:).md)
  Notifies the delegate that the specified item is about to be displayed by the collection view.
- [func collectionView(NSCollectionView, didEndDisplaying: NSCollectionViewItem, forRepresentedObjectAt: IndexPath)](nscollectionviewdelegate/collectionview(_:didenddisplaying:forrepresentedobjectat:).md)
  Notifies the delegate that the specified item was removed from the collection view.
- [func collectionView(NSCollectionView, willDisplaySupplementaryView: NSView, forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath)](nscollectionviewdelegate/collectionview(_:willdisplaysupplementaryview:forelementkind:at:).md)
  Notifies the delegate that the specified supplementary view is about to be displayed by the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:))*