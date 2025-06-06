# layoutAttributesForDecorationView(ofKind:at:)

**Framework**: AppKit  
**Kind**: method

Returns the layout attributes of the decoration view at the specified location in your layout.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func layoutAttributesForDecorationView(ofKind elementKind: NSCollectionView.DecorationElementKind, at indexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

#### Return Value

A layout attributes object containing the layout information to apply to the decoration view.

#### Discussion

If your layout includes decoration views, you must override this method. In your implementation, create an instance of the appropriate layout attributes class and fill the resulting object with the layout information for the corresponding decoration view. You define the supported decoration views by assigning each one a string that identifies its kind. Use the `elementKind` and `indexPath` properties to identify the specific decoration view whose attributes were requested.

You can call this method from other layout-related methods when you want to retrieve layout information for decoration views. Call this method only for decoration views. Do not call it to retrieve layout attributes for items or supplementary views.

## Parameters

- `elementKind`: A string that identifies the type of the decoration view. Use this string to differentiate the decoration views in a given section.
- `indexPath`: The index path of the decoration view. Use this parameter to determine which section contains the decoration view.

## See Also

- [class var layoutAttributesClass: AnyClass](nscollectionviewlayout/layoutattributesclass.md)
  Returns the class to use for layout attribute objects
- [func prepare()](nscollectionviewlayout/prepare.md)
  Prepares the layout object to begin laying out content.
- [var collectionViewContentSize: NSSize](nscollectionviewlayout/collectionviewcontentsize.md)
  The width and height of the collection view’s contents.
- [func layoutAttributesForElements(in: NSRect) -> [NSCollectionViewLayoutAttributes]](nscollectionviewlayout/layoutattributesforelements(in:).md)
  Returns the layout attribute objects for all items and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforitem(at:).md)
  Returns the layout attributes for the item at the specified index path.
- [func layoutAttributesForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md)
  Returns the layout attributes of the supplementary view at the specified location in your layout.
- [func layoutAttributesForDropTarget(at: NSPoint) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesfordroptarget(at:).md)
  Returns layout attributes for the drop target at the specified point.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforinteritemgap(before:).md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:))*