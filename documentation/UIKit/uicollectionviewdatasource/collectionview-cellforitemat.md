# collectionView(_:cellForItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks your data source object for the cell that corresponds to the specified item in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell
```

#### Return Value

A configured cell object. You must not return `nil` from this method.

#### Discussion

Your implementation of this method is responsible for creating, configuring, and returning the appropriate cell for the given item. You do this by calling the [`dequeueReusableCell(withReuseIdentifier:for:)`](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md) method of the collection view and passing the reuse identifier that corresponds to the cell type you want. That method always returns a valid cell object. Upon receiving the cell, you should set any properties that correspond to the data of the corresponding item, perform any additional needed configuration, and return the cell.

You don’t need to set the location of the cell inside the collection view’s bounds. The collection view sets the location of each cell automatically using the layout attributes provided by its layout object.

If [`isPrefetchingEnabled`](uicollectionview/isprefetchingenabled.md) on the collection view is set to [`true`](https://developer.apple.com/documentation/swift/true) then this method is called in advance of the cell appearing. Use the [`collectionView(_:willDisplay:forItemAt:)`](uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:).md) delegate method to make any changes to the appearance of the cell to reflect its visual state such as selection.

This method must always return a valid view object.

## Parameters

- `collectionView`: The collection view requesting this information.
- `indexPath`: The index path that specifies the location of the item.

## See Also

- [func collectionView(UICollectionView, viewForSupplementaryElementOfKind: String, at: IndexPath) -> UICollectionReusableView](uicollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:).md)
  Asks your data source object to provide a supplementary view to display in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:cellforitemat:))*