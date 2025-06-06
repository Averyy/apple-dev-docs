# NSCollectionLayoutVisibleItem

**Framework**: UIKit  
**Kind**: protocol

An item that’s currently visible within the bounds of a section.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol NSCollectionLayoutVisibleItem : UIDynamicItem
```

#### Overview

A visible item represents an item in a collection view that’s currently visible onscreen, such as a cell, supplementary view, or decoration. You access a specific section’s visible items in its visible item invalidation handler ([`NSCollectionLayoutSectionVisibleItemsInvalidationHandler`](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)), stored in the [`visibleItemsInvalidationHandler`](nscollectionlayoutsection/visibleitemsinvalidationhandler.md) property. The handler is called before each layout cycle, any time an animation occurs in that section due to changes such as adding or removing items, scrolling the section, or rotating the device.

## Topics

### Identifying the item
- [var name: String](nscollectionlayoutvisibleitem/name.md)
  The name of the item.
- [var representedElementKind: String?](nscollectionlayoutvisibleitem/representedelementkind.md)
  A string that identifies the type of item.
- [var representedElementCategory: UICollectionView.ElementCategory](nscollectionlayoutvisibleitem/representedelementcategory.md)
  A category that identifies the item, such as decoration or supplementary view.
### Getting the index path
- [var indexPath: IndexPath](nscollectionlayoutvisibleitem/indexpath.md)
  The index path of the item.
### Configuring appearance
- [var alpha: CGFloat](nscollectionlayoutvisibleitem/alpha.md)
  The transparency of the item.
- [var isHidden: Bool](nscollectionlayoutvisibleitem/ishidden.md)
  A Boolean value that determines whether the item is hidden.
### Configuring position
- [var frame: CGRect](nscollectionlayoutvisibleitem/frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var bounds: CGRect](nscollectionlayoutvisibleitem/bounds.md)
  The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [var center: CGPoint](nscollectionlayoutvisibleitem/center.md)
  The center point of the item’s frame rectangle.
- [var transform: CGAffineTransform](nscollectionlayoutvisibleitem/transform.md)
  The transform applied to the item, relative to the center of its bounds.
- [var transform3D: CATransform3D](nscollectionlayoutvisibleitem/transform3d.md)
  The 3D transform applied to the item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutvisibleitem/zindex.md)
  The vertical stacking order of the item in relation to other items in the section.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDynamicItem](uidynamicitem.md)

## See Also

- [typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)
  A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [class UICollectionViewUpdateItem](uicollectionviewupdateitem.md)
  An object that describes a single change to make to an item in a collection view.
- [class UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md)
  A context object that stores information specific to a focus update in a collection view.
- [class UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md)
  A context object that declares which parts of your layout need to be updated when the layout is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem)*