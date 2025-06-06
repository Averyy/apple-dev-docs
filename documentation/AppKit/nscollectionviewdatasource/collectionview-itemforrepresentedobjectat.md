# collectionView(_:itemForRepresentedObjectAt:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks your data source object to provide the item at the specified location in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: NSCollectionView, itemForRepresentedObjectAt indexPath: IndexPath) -> NSCollectionViewItem
```

#### Return Value

A configured item object. You must not return `nil` from this method.

#### Discussion

All data source objects must implement this method. Your implementation is responsible for creating, configuring, and returning the appropriate item object based on the specified index path. You do this by calling the [`makeItem(withIdentifier:for:)`](nscollectionview/makeitem(withidentifier:for:).md) method of the collection view to retrieve an empty item object of the appropriate type. After receiving the item object, update its properties with the data from your app’s data structures and return it.

You do not need to set the frame of an item’s view from this method. The collection view gets the item’s location and other layout-related attributes from the layout object during a separate step.

## Parameters

- `collectionView`: The collection view requesting the information.
- `indexPath`: The index path that specifies the location of the item. This index path contains both the section index and the item index within that section.

## See Also

- [func collectionView(NSCollectionView, viewForSupplementaryElementOfKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSView](nscollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:).md)
  Asks your data source object to provide the supplementary view at the specified location in a section of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdatasource/collectionview(_:itemforrepresentedobjectat:))*