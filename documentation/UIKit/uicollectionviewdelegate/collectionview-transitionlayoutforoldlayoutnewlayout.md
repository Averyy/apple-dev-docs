# collectionView(_:transitionLayoutForOldLayout:newLayout:)

**Framework**: UIKit  
**Kind**: method

Asks for the custom transition layout to use when moving between the specified layouts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout
```

#### Return Value

The collection view transition layout object to use to perform the transition.

#### Discussion

Implement this method if you want to return a custom [`UICollectionViewTransitionLayout`](uicollectionviewtransitionlayout.md) object for use during the transition. A transition layout object lets you customize the behavior of cells and decoration views when transitioning from one layout to the next. Normally, transitioning between layouts causes items to animate directly from their current locations to their new locations. With a transition layout object, you can have objects follow a non linear path, use a different timing algorithm, or move according to incoming touch events.

If your delegate does not implement this method, the collection view creates a standard [`UICollectionViewTransitionLayout`](uicollectionviewtransitionlayout.md) object and uses that object to manage the transition.

## Parameters

- `collectionView`: The collection view whose layout object is changing.
- `fromLayout`: The current layout of the collection view. This is the starting point for the transition.
- `toLayout`: The new layout for the collection view.

## See Also

- [func collectionView(UICollectionView, targetContentOffsetForProposedContentOffset: CGPoint) -> CGPoint](uicollectionviewdelegate/collectionview(_:targetcontentoffsetforproposedcontentoffset:).md)
  Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.
- [func collectionView(UICollectionView, targetIndexPathForMoveOfItemFromOriginalIndexPath: IndexPath, atCurrentIndexPath: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformoveofitemfromoriginalindexpath:atcurrentindexpath:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:transitionlayoutforoldlayout:newlayout:))*