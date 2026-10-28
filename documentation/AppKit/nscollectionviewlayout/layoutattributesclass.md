# layoutAttributesClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the class to use for layout attribute objects

**Availability**:
- macOS

## Declaration

```swift
class var layoutAttributesClass: AnyClass { get }
```

```objc
@property (class, readonly) Class layoutAttributesClass;
```

## Return Value

The class to use for layout attribute objects.

## Discussion

Override this method if you define a custom [`NSCollectionViewLayoutAttributes`](../nscollectionviewlayoutattributes.md) subclass for managing layout-related attributes. In your implementation, return the class object for your custom subclass.

You can call this method as needed to create new layout objects. A typical usage of this method is as follows:

**Swift**:

```swift
let attributes = MyCustomLayout.layoutAttributesClass().init()
```

**Objective-C**:

```objc
id attributes = [[[MyCustomLayout layoutAttributesClass] alloc] init];
```

## See Also

### Providing Layout Information
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
- [func layoutAttributesForDropTarget(at: NSPoint) -> NSCollectionViewLayoutAttributes?](./layoutattributesfordroptarget%28at%29.md)
  Returns layout attributes for the drop target at the specified point.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](./layoutattributesforinteritemgap%28before%29.md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset%29.md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/layoutattributesclass)*