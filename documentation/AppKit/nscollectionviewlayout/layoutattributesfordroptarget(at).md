# layoutAttributesForDropTarget(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns layout attributes for the drop target at the specified point.

**Availability**:
- macOS

## Declaration

```swift
func layoutAttributesForDropTarget(at pointInCollectionView: NSPoint) -> NSCollectionViewLayoutAttributes?
```

```objc
- (NSCollectionViewLayoutAttributes *) layoutAttributesForDropTargetAtPoint:(NSPoint) pointInCollectionView;
```

## Return Value

A layout attributes object that identifies the element in which the drop would occur.

## Discussion

The default implementation of this method tests the specified point to see if it lands inside an item, supplementary view, or decoration view of the collection view. If it does, the method returns the layout attributes for that element.

Layouts that support inter-item gaps as drop targets must override this method and use it to return the layout attributes that represent that gap. In your implementation, calculate the index path just after the gap and pass that value to the [`init(forInterItemGapBefore:)`](../nscollectionviewlayoutattributes/init%28forinteritemgapbefore%29.md) class method of [`NSCollectionViewLayoutAttributes`](../nscollectionviewlayoutattributes.md). Set the [`frame`](../nscollectionviewlayoutattributes/frame.md) property of the resulting attributes object to the rectangle that best represents the gap and also contains the specified point. When overriding this method, you can call `super` at any time to get the default behavior.

## Parameters

- `pointInCollectionView`: A point in the collection view’s coordinate system. Use this point to determine whether the drop would occur on an item or between items.

## See Also

### Providing Layout Information
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  Returns the class to use for layout attribute objects
- [func prepare()](./prepare%28%29.md)
  Prepares the layout object to begin laying out content.
- [var collectionViewContentSize: NSSize](./collectionviewcontentsize.md)
  The width and height of the collection view’s contents.
- [func layoutAttributesForElements(in: NSRect) -> [NSCollectionViewLayoutAttributes]](./layoutattributesforelements%28in%29.md)
  Returns the layout attribute objects for all items and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforitem%28at%29.md)
  Returns the layout attributes for the item at the specified index path.
- [func layoutAttributesForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforsupplementaryview%28ofkind,at%29.md)
  Returns the layout attributes of the supplementary view at the specified location in your layout.
- [func layoutAttributesForDecorationView(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  Returns the layout attributes of the decoration view at the specified location in your layout.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforinteritemgap%28before%29.md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset%29.md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/layoutattributesfordroptarget(at:))*