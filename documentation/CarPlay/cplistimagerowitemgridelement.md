# CPListImageRowItemGridElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row element that displays an image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemGridElement
```

```objc
@interface CPListImageRowItemGridElement : CPListImageRowItemElement
```

## Overview

The `CPListImageRowItemGridElement ` class defines an element you add to a row in a list template. Use this class with the [`CPListImageRowItem`](./cplistimagerowitem.md) type to include more content in each row of your list. This element type displays an image for the specified item without any additional text.

When building a list interface, create instances of this class and use them to populate your [`CPListImageRowItem`](./cplistimagerowitem.md) type. To handle row-related interactions with elements in a row, configure the [`listImageRowHandler`](./cplistimagerowitem/listimagerowhandler.md) property of the row itself.

## Topics

### Creating a grid element
- [init(image: UIImage)](./cplistimagerowitemgridelement/init%28image%29.md)
  Creates a grid row element with the specified image.

## Relationships

### Inherits From
- [CPListImageRowItemElement](./cplistimagerowitemelement.md)
### Conforms To
- [CPPlayableItem](./cpplayableitem.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Row elements
- [class CPListImageRowItemRowElement](./cplistimagerowitemrowelement.md)
  A row element that displays an image, title, and subtitle.
- [class CPListImageRowItemCardElement](./cplistimagerowitemcardelement.md)
  A row element that displays an image and text on a card-style background.
- [class CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
  A row element that displays an image and text in a vertically condensed style.
- [class CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
  A row element that displays an image with a custom cutout shape and a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemgridelement)*