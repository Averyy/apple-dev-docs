# NSCollectionLayoutSupplementaryItem

**Framework**: AppKit  
**Kind**: class

An object used to add an extra visual decoration to an item in a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSupplementaryItem
```

#### Overview

You use supplementary items to attach additional views to your content. For example, you might attach a badge to an item or a frame around a group. A supplementary item follows the index path of the item it’s attached to.

If you want to create a header or footer for your layout or its sections, use a boundary supplementary item (<````NSCollectionLayoutBoundarySupplementaryItem``>) instead.

Each type of supplementary item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

Add supplementary items to an item by passing in an array of supplementary items when you construct the item:

## Topics

### Creating a supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor)](nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:).md)
  Creates a supplementary item of the specified size and element kind, with an anchor relative to a container.
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor, itemAnchor: NSCollectionLayoutAnchor)](nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:itemanchor:).md)
  Creates a supplementary item of the specified size and element kind, an anchor relative to a container, and an anchor relative to an item.
### Getting the anchors
- [var itemAnchor: NSCollectionLayoutAnchor?](nscollectionlayoutsupplementaryitem/itemanchor.md)
  The anchor between the supplementary item and the item it’s attached to.
- [var containerAnchor: NSCollectionLayoutAnchor](nscollectionlayoutsupplementaryitem/containeranchor.md)
  The anchor between the supplementary item and the container it’s attached to.
### Getting the element kind
- [var elementKind: String](nscollectionlayoutsupplementaryitem/elementkind.md)
  A string that identifies the type of supplementary item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutsupplementaryitem/zindex.md)
  The vertical stacking order of the supplementary item in relation to other items in the section.

## Relationships

### Inherits From
- [NSCollectionLayoutItem](nscollectionlayoutitem.md)
### Inherited By
- [NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.
- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsupplementaryitem)*