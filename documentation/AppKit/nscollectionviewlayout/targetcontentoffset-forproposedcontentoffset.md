# targetContentOffset(forProposedContentOffset:)

**Framework**: AppKit  
**Kind**: method

Returns the offset value to use after an animated layout update or change.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func targetContentOffset(forProposedContentOffset proposedContentOffset: NSPoint) -> NSPoint
```

#### Return Value

The offset value that you want to use for the content.

#### Discussion

During layout updates, or when transitioning between layouts, the collection view calls this method to give you the opportunity to tweak the position of the collection view’s content at the end of animations. The default implementation of this method returns the value in the `proposedContentOffset` parameter. Subclasses can override it and return an offset value that positions content in a way that is more optimal for the custom layout.

## Parameters

- `proposedContentOffset`: The proposed point (in the collection view’s coordinate space) for the lower-left corner of the visible content. The collection view calculates this value as the most likely value to use at the end of animations.

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
- [func layoutAttributesForDecorationView(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md)
  Returns the layout attributes of the decoration view at the specified location in your layout.
- [func layoutAttributesForDropTarget(at: NSPoint) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesfordroptarget(at:).md)
  Returns layout attributes for the drop target at the specified point.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforinteritemgap(before:).md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:))*