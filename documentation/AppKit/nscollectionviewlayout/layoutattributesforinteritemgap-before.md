# layoutAttributesForInterItemGap(before:)

**Framework**: AppKit  
**Kind**: method

Returns layout attributes for the inter-item gap at the specified location in your layout.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func layoutAttributesForInterItemGap(before indexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

#### Return Value

A layout attributes object containing the layout information to apply to the inter-item gap, or `nil` if no attributes are available.

#### Discussion

The default implementation of this method returns `nil`. Subclasses can override this method to provide layout attributes for inter-item gaps. In your implementation, use the specified index path to compute the location of the gap in collection view’s content. If the gap represents a valid location, use the [`init(forInterItemGapBefore:)`](nscollectionviewlayoutattributes/init(forinteritemgapbefore:).md) class method of [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md) to create a new layout attributes object and set the [`frame`](nscollectionviewlayoutattributes/frame.md) property to the rectangle you computed.

## Parameters

- `indexPath`: The index path of the item that follows the inter-item gap. For a gap that follows the last item in the section, set the item property to the total number of items in the section.

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
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/layoutattributesforinteritemgap(before:))*