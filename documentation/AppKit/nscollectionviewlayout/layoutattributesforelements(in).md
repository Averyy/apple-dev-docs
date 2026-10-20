# layoutAttributesForElements(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the layout attribute objects for all items and views in the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func layoutAttributesForElements(in rect: NSRect) -> [NSCollectionViewLayoutAttributes]
```

```objc
- (NSArray<__kindof NSCollectionViewLayoutAttributes *> *) layoutAttributesForElementsInRect:(NSRect) rect;
```

#### Return Value

An array of layout attribute objects containing the layout information for the enclosed items and views.

#### Discussion

Subclasses must override this method. In your implementation, return layout attributes for all items, supplementary views, and decoration views that intersect the specified rectangle.

For each element, always return a layout object of the appropriate type (item, supplementary, or decoration). The collection view differentiates between attributes for items, supplementary views, and decoration views and uses the differences to decide how to create and manage the corresponding views. Use the [`layoutAttributesForItem(at:)`](./layoutattributesforitem%28at%29.md), [`layoutAttributesForSupplementaryView(ofKind:at:)`](./layoutattributesforsupplementaryview%28ofkind,at%29.md), and [`layoutAttributesForDecorationView(ofKind:at:)`](./layoutattributesfordecorationview%28ofkind,at%29.md) methods to create new layout attribute objects.

## Parameters

- `rect`: The rectangle (specified in the collection view’s coordinate system) containing the target views.

## See Also

### Providing Layout Information
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  Returns the class to use for layout attribute objects
- [func prepare()](./prepare%28%29.md)
  Prepares the layout object to begin laying out content.
- [var collectionViewContentSize: NSSize](./collectionviewcontentsize.md)
  The width and height of the collection view’s contents.
- [func layoutAttributesForItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforitem%28at%29.md)
  Returns the layout attributes for the item at the specified index path.
- [func layoutAttributesForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforsupplementaryview%28ofkind,at%29.md)
  Returns the layout attributes of the supplementary view at the specified location in your layout.
- [func layoutAttributesForDecorationView(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  Returns the layout attributes of the decoration view at the specified location in your layout.
- [func layoutAttributesForDropTarget(at: NSPoint) -> NSCollectionViewLayoutAttributes?](./layoutattributesfordroptarget%28at%29.md)
  Returns layout attributes for the drop target at the specified point.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforinteritemgap%28before%29.md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset%29.md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/layoutattributesforelements(in:))*