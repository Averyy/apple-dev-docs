# NSCollectionLayoutEdgeSpacing

**Framework**: UIKit  
**Kind**: class

An object that defines the space around the edges of items in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutEdgeSpacing
```

#### Overview

You use edge spacing to create additional spacing around the edges of an item to adjust the position of the item in relation to its container and other items.

The leading and trailing spaces within edge spacing differ in left-to-right versus right-to-left environments. In a left-to-right environment, the leading space is on the left, and the trailing space is on the right. In a right-to-left environment, the leading space is on the right, and the trailing space is on the left. This difference ensures that your collection view layout is built with support for right-to-left languages.

The following diagram shows the difference between adding 2 points of trailing edge spacing in a left-to-right versus a right-to-left environment.

![Two diagrams that compare edge spacing in a left-to-right and a right-to-left environment. Both diagrams show a group of three square items in a row. The first diagram, labeled trailing in left-to-right environment, shows trailing space on the right of each item, implying that leading space is on the left. The second diagram, labeled trailing in right-to-left environment, shows trailing space on the left of each item, implying that leading space is on the right.](https://docs-assets.developer.apple.com/published/a315a0a064f715f044a87ad23b139457/media-3570381%402x.png)

## Topics

### Creating edge spacing
- [convenience init(leading: NSCollectionLayoutSpacing?, top: NSCollectionLayoutSpacing?, trailing: NSCollectionLayoutSpacing?, bottom: NSCollectionLayoutSpacing?)](nscollectionlayoutedgespacing/init(leading:top:trailing:bottom:).md)
  Creates an edge spacing object with the specified leading, top, trailing, and bottom spacing.
### Getting the edge spacing
- [var leading: NSCollectionLayoutSpacing?](nscollectionlayoutedgespacing/leading.md)
  The leading edge spacing value.
- [var top: NSCollectionLayoutSpacing?](nscollectionlayoutedgespacing/top.md)
  The top edge spacing value.
- [var trailing: NSCollectionLayoutSpacing?](nscollectionlayoutedgespacing/trailing.md)
  The trailing edge spacing value.
- [var bottom: NSCollectionLayoutSpacing?](nscollectionlayoutedgespacing/bottom.md)
  The bottom edge spacing value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSCollectionLayoutDimension](nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSize](nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutSpacing](nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [protocol NSCollectionLayoutContainer](nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutedgespacing)*