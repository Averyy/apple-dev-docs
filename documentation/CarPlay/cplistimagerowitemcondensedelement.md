# CPListImageRowItemCondensedElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row element that displays an image and text in a vertically condensed style.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemCondensedElement
```

```objc
@interface CPListImageRowItemCondensedElement : CPListImageRowItemElement
```

## Overview

The `CPListImageRowItemCondensedElement ` class defines an element you add to a row in a list template. Use this class in conjunction with the [`CPListImageRowItem`](./cplistimagerowitem.md) type to include more content in each row of your list. This element type displays a required image, a title string, and an optional subtitle in a vertically compressed layout on a system-provided background.

When building a list interface, create instances of this class and use them to populate your [`CPListImageRowItem`](./cplistimagerowitem.md) type. To handle row-related interactions with elements in a row, configure the [`listImageRowHandler`](./cplistimagerowitem/listimagerowhandler.md) property of the row itself.

## Topics

### Creating a condensed element
- [init(image: UIImage, imageShape: CPListImageRowItemCondensedElement.Shape, title: String, subtitle: String?, accessorySymbolName: String?)](./cplistimagerowitemcondensedelement/init%28image,imageshape,title,subtitle,accessorysymbolname%29.md)
  Creates a condensed row element with the specified image, text, and attributes.
### Getting the element’s content
- [var title: String](./cplistimagerowitemcondensedelement/title.md)
  The primary text for the element.
- [var subtitle: String?](./cplistimagerowitemcondensedelement/subtitle.md)
  The secondary text for the element.
- [var accessorySymbolName: String?](./cplistimagerowitemcondensedelement/accessorysymbolname.md)
  The name of an image to display at the trailing edge of the element.
### Getting the element’s shape
- [var imageShape: CPListImageRowItemCondensedElement.Shape](./cplistimagerowitemcondensedelement/imageshape.md)
  The shape to apply to the current element’s image.
- [CPListImageRowItemCondensedElement.Shape](./cplistimagerowitemcondensedelement/shape.md)
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
- [class CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
  A row element that displays an image.
- [class CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
  A row element that displays an image with a custom cutout shape and a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement)*