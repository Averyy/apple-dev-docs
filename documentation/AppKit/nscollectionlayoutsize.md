# NSCollectionLayoutSize

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The width and the height of an item in a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSize
```

```objc
@interface NSCollectionLayoutSize : NSObject
```

#### Overview

A size is a pair of dimensions ([`NSCollectionLayoutDimension`](./nscollectionlayoutdimension.md)): a width dimension and a height dimension. Every component of a collection view layout has an explicit size.

## Topics

### Creating a layout size
- [convenience init(widthDimension: NSCollectionLayoutDimension, heightDimension: NSCollectionLayoutDimension)](./nscollectionlayoutsize/init%28widthdimension,heightdimension%29.md)
  Creates a size with the specified width and height dimensions.
### Getting the width and height
- [var widthDimension: NSCollectionLayoutDimension](./nscollectionlayoutsize/widthdimension.md)
  The width dimension of an item in a collection view layout.
- [var heightDimension: NSCollectionLayoutDimension](./nscollectionlayoutsize/heightdimension.md)
  The height dimension of an item in a collection view layout.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Size and spacing
- [class NSCollectionLayoutDimension](./nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSpacing](./nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [class NSCollectionLayoutEdgeSpacing](./nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](./nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsize)*