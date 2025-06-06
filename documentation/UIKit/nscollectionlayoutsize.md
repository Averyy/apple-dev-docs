# NSCollectionLayoutSize

**Framework**: UIKit  
**Kind**: class

The width and the height of an item in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSize
```

#### Overview

A size is a pair of dimensions ([`NSCollectionLayoutDimension`](nscollectionlayoutdimension.md)): a width dimension and a height dimension. Every component of a collection view layout has an explicit size.

## Topics

### Creating a layout size
- [convenience init(widthDimension: NSCollectionLayoutDimension, heightDimension: NSCollectionLayoutDimension)](nscollectionlayoutsize/init(widthdimension:heightdimension:).md)
  Creates a size with the specified width and height dimensions.
### Getting the width and height
- [var widthDimension: NSCollectionLayoutDimension](nscollectionlayoutsize/widthdimension.md)
  The width dimension of an item in a collection view layout.
- [var heightDimension: NSCollectionLayoutDimension](nscollectionlayoutsize/heightdimension.md)
  The height dimension of an item in a collection view layout.

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
- [class NSCollectionLayoutSpacing](nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [class NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsize)*