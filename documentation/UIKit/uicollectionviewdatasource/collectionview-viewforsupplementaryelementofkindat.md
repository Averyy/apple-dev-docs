# collectionView(_:viewForSupplementaryElementOfKind:at:)

**Framework**: UIKit  
**Kind**: method

Asks your data source object to provide a supplementary view to display in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView
```

#### Return Value

A configured supplementary view object. You must not return `nil` from this method.

#### Discussion

Your implementation of this method is responsible for creating, configuring, and returning the appropriate supplementary view that is being requested. You do this by calling the [`dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)`](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md) method of the collection view and passing the information that corresponds to the view you want. That method always returns a valid view object. Upon receiving the view, you should set any properties that correspond to the data you want to display, perform any additional needed configuration, and return the view.

You do not need to set the location of the supplementary view inside the collection view’s bounds. The collection view sets the location of each view using the layout attributes provided by its layout object.

This method must always return a valid view object. If you do not want a supplementary view in a particular case, your layout object should not create the attributes for that view. Alternatively, you can hide views by setting the [`isHidden`](uicollectionviewlayoutattributes/ishidden.md) property of the corresponding attributes to [`true`](https://developer.apple.com/documentation/Swift/true) or set the [`alpha`](uicollectionviewlayoutattributes/alpha.md) property of the attributes to 0. To hide header and footer views in a flow layout, you can also set the width and height of those views to 0.

## Parameters

- `collectionView`: The collection view requesting this information.
- `kind`: The kind of supplementary view to provide. The value of this string is defined by the layout object that supports the supplementary view.
- `indexPath`: The index path that specifies the location of the new supplementary view.

## See Also

- [func collectionView(UICollectionView, cellForItemAt: IndexPath) -> UICollectionViewCell](uicollectionviewdatasource/collectionview(_:cellforitemat:).md)
  Asks your data source object for the cell that corresponds to the specified item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:))*