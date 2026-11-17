# CPListImageRowItemImageGridElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row element that displays an image with a custom cutout shape and a title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemImageGridElement
```

```objc
@interface CPListImageRowItemImageGridElement : CPListImageRowItemElement
```

## Overview

The `CPListImageRowItemImageGridElement ` class defines an element you add to a row in a list template. Use this class in conjunction with the [`CPListImageRowItem`](./cplistimagerowitem.md) type to include more content in each row of your list. This element type displays an image for the specified item with a title string below the image. You can also include an SF Symbol or other image to display next to the title. For example, you might display the “heart.fill” SF Symbol next to someone’s favorite items.

When building a list interface, create instances of this class and use them to populate your [`CPListImageRowItem`](./cplistimagerowitem.md) type. To handle row-related interactions with elements in a row, configure the [`listImageRowHandler`](./cplistimagerowitem/listimagerowhandler.md) property of the row itself.

## Topics

### Creating a grid element
- [init(image: UIImage, imageShape: CPListImageRowItemImageGridElement.Shape, title: String, accessorySymbolName: String?)](./cplistimagerowitemimagegridelement/init%28image,imageshape,title,accessorysymbolname%29.md)
  Creates a row element with the specified image, text, and attributes.
### Getting the element’s content
- [var title: String](./cplistimagerowitemimagegridelement/title.md)
  The primary text for the element.
- [var accessorySymbolName: String?](./cplistimagerowitemimagegridelement/accessorysymbolname.md)
  The name of an image to display next to the element’s title.
### Getting the element’s shape
- [var imageShape: CPListImageRowItemImageGridElement.Shape](./cplistimagerowitemimagegridelement/imageshape.md)
  The shape to apply to the current element’s image.
- [CPListImageRowItemImageGridElement.Shape](./cplistimagerowitemimagegridelement/shape.md)
  Shapes you can apply to an element’s image.

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
- [class CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
  A row element that displays an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemimagegridelement)*