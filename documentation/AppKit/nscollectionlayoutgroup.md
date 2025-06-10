# NSCollectionLayoutGroup

**Framework**: AppKit  
**Kind**: class

A container for a set of items that lays out the items along a path.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutGroup
```

#### Overview

Groups determine how the items in a collection view lay out in relation to each other. A group might lay out its items in a horizontal row, a vertical column, or a custom arrangement. A group determines the rules for how items are rendered in relation to each other, but in itself doesn’t render any content.

For example, in the Photos app, a group of items is a row of photos. In the App Store app, a group might be a single column of cells (items) arranged in a vertical column.

![Schematic representation of the App Store app on iOS, showing a collection view with a compositional layout. The layout is composed of horizontally-scrolling sections that have different layouts. The top section shows one group with one item visible onscreen, with other groups peeking in from the sides of the screen. The bottom section shows one group that’s a column of three cells, each of those cells being an item. The two different types of groups are highlighted and labeled as groups.](https://docs-assets.developer.apple.com/published/fc57f40cd933b8fdf6ee5bc26e52d7fa/media-3568663%402x.png)

Each group specifies its own size in terms of a width dimension and a height dimension. Groups can express their dimensions relative to their container, as an absolute value, or as an estimated value that might change at runtime, like in response to a change in system font size. For more information, see [`NSCollectionLayoutDimension`](nscollectionlayoutdimension.md).

Because a group is a subclass of [`NSCollectionLayoutItem`](nscollectionlayoutitem.md), it behaves like an item. You can combine a group with other items and groups into more complex layouts.

![Illustration of group nesting in a compositional layout. A larger group contains one large item on the leading side and two smaller items stacked vertically in a nested group on the trailing side.](https://docs-assets.developer.apple.com/published/47daaa6eb89261c15d6bcb264846aa1b/media-3568666%402x.png)

After you configure a group, you must initialize a section ([`NSCollectionLayoutSection`](nscollectionlayoutsection.md)) of your collection view layout with that group.

## Topics

### Creating a horizontal group
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](nscollectionlayoutgroup/horizontal(layoutsize:subitems:).md)
  Creates a group of the specified size, containing an array of items arranged in a horizontal line.
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](nscollectionlayoutgroup/horizontal(layoutsize:subitem:count:).md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.
### Creating a vertical group
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitems:).md)
  Creates a group of the specified size, containing an array of items arranged in a vertical line.
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitem:count:).md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.
### Creating a custom group
- [class func custom(layoutSize: NSCollectionLayoutSize, itemProvider: NSCollectionLayoutGroupCustomItemProvider) -> Self](nscollectionlayoutgroup/custom(layoutsize:itemprovider:).md)
  Creates a group of the specified size, with an item provider that creates a custom arrangement for those items.
### Getting the group’s items
- [var subitems: [NSCollectionLayoutItem]](nscollectionlayoutgroup/subitems.md)
  An array of the items contained in the group.
- [var supplementaryItems: [NSCollectionLayoutSupplementaryItem]](nscollectionlayoutgroup/supplementaryitems.md)
  An array of the supplementary items that are anchored to the group.
### Configuring group spacing
- [var interItemSpacing: NSCollectionLayoutSpacing?](nscollectionlayoutgroup/interitemspacing.md)
  The amount of space between the items in the group.
### Debugging group layout
- [func visualDescription() -> String](nscollectionlayoutgroup/visualdescription.md)
  Returns a string with an ASCII representation of the group.

## Relationships

### Inherits From
- [NSCollectionLayoutItem](nscollectionlayoutitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSCollectionLayoutItem](nscollectionlayoutitem.md)
  The most basic component of a collection view’s layout.
- [class NSCollectionLayoutSection](nscollectionlayoutsection.md)
  A container that combines a set of groups into distinct visual groupings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup)*