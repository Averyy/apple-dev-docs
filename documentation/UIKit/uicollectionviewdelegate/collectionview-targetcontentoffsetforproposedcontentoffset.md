# collectionView(_:targetContentOffsetForProposedContentOffset:)

**Framework**: UIKit  
**Kind**: method

Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, targetContentOffsetForProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint
```

#### Return Value

The content offset that you want to use instead. If you do not implement this method, the collection view uses the value in the `proposedContentOffset` parameter.

#### Discussion

During layout updates, or when transitioning between layouts, the collection view calls this method to give you the opportunity to change the proposed content offset to use at the end of the animation. You might return a new value if the layout or animations might cause items to be positioned in a way that is not optimal for your design.

This method is called after the layout object’s [`targetContentOffset(forProposedContentOffset:)`](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md) method. Implement this method in situations where you do not want to subclass your layout object to modify the content offset.

## Parameters

- `collectionView`: The collection view making the request.
- `proposedContentOffset`: The proposed point (in the coordinate space of the collection view’s content view) for the upper-left corner of the visible content. This represents the point that the collection view has calculated as the most likely value to use for the animations or layout update.

## See Also

- [func collectionView(UICollectionView, transitionLayoutForOldLayout: UICollectionViewLayout, newLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout](uicollectionviewdelegate/collectionview(_:transitionlayoutforoldlayout:newlayout:).md)
  Asks for the custom transition layout to use when moving between the specified layouts.
- [func collectionView(UICollectionView, targetIndexPathForMoveOfItemFromOriginalIndexPath: IndexPath, atCurrentIndexPath: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformoveofitemfromoriginalindexpath:atcurrentindexpath:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetcontentoffsetforproposedcontentoffset:))*