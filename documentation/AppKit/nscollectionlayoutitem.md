# NSCollectionLayoutItem

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The most basic component of a collection view’s layout.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutItem
```

```objc
@interface NSCollectionLayoutItem : NSObject
```

#### Overview

An item is a blueprint for how to size, space, and arrange an individual piece of content in your collection view. An item represents a single view that’s rendered onscreen. Generally, an item is a cell, but items can be supplementary views like headers, footers, and other decorations.

For example, in the Photos app, an item might represent a single photo. In the App Store app, an item might be a cell displaying information about an individual app in a list of featured apps, such as the app icon, app name, tagline, and download button.

![Schematic representation of the App Store app on iOS, showing a collection view with a compositional layout. The layout is composed of two horizontally-scrolling sections that have different layouts. The top section shows one group with one item visible onscreen, with other groups peeking in from the sides of the screen. The bottom section shows one group that’s a column of three cells, each of those cells being an item. The two different types of items are highlighted and labeled as items.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-3568665@2x.png)

Each item specifies its own size in terms of a width dimension and a height dimension. Items can express their dimensions relative to their container, as an absolute value, or as an estimated value that might change at runtime, like in response to a change in system font size. For more information, see [`NSCollectionLayoutDimension`](./nscollectionlayoutdimension.md).

You combine items into groups that determine how those items are arranged in relation to each other. For more information, see [`NSCollectionLayoutGroup`](./nscollectionlayoutgroup.md).

## Topics

### Creating an item
- [convenience init(layoutSize: NSCollectionLayoutSize)](./nscollectionlayoutitem/init%28layoutsize%29.md)
  Creates an item of the specified size.
- [convenience init(layoutSize: NSCollectionLayoutSize, supplementaryItems: [NSCollectionLayoutSupplementaryItem])](./nscollectionlayoutitem/init%28layoutsize,supplementaryitems%29.md)
  Creates an item of the specified size with an array of supplementary items to attach to the item.
### Getting an item’s size
- [var layoutSize: NSCollectionLayoutSize](./nscollectionlayoutitem/layoutsize.md)
  The item’s size expressed in width and height dimensions.
### Getting supplementary items
- [var supplementaryItems: [NSCollectionLayoutSupplementaryItem]](./nscollectionlayoutitem/supplementaryitems.md)
  An array of the supplementary items attached to the item.
### Configuring spacing and insets
- [var edgeSpacing: NSCollectionLayoutEdgeSpacing?](./nscollectionlayoutitem/edgespacing.md)
  The amount of space added around the boundaries of the item between other items and this item’s container.
- [var contentInsets: NSDirectionalEdgeInsets](./nscollectionlayoutitem/contentinsets.md)
  The amount of space added around the content of the item to adjust its final size after its position is computed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSCollectionLayoutDecorationItem](./nscollectionlayoutdecorationitem.md)
- [NSCollectionLayoutGroup](./nscollectionlayoutgroup.md)
- [NSCollectionLayoutSupplementaryItem](./nscollectionlayoutsupplementaryitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Components
- [class NSCollectionLayoutGroup](./nscollectionlayoutgroup.md)
  A container for a set of items that lays out the items along a path.
- [class NSCollectionLayoutSection](./nscollectionlayoutsection.md)
  A container that combines a set of groups into distinct visual groupings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutitem)*