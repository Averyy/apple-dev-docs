# CPListImageRowItemRowElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row element that displays an image, title, and subtitle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemRowElement
```

```objc
@interface CPListImageRowItemRowElement : CPListImageRowItemElement
```

## Overview

The `CPListImageRowItemRowElement` class defines an element you add to a row in a list template. Use this class in conjunction with the [`CPListImageRowItem`](./cplistimagerowitem.md) type to include more content in each row of your list. This element type displays a required image and an optional title and subtitle on top of the standard background. Provide the text values when possible to add meaningful information. For example, an element displaying the artwork for an album might display the album’s name and band information in the text fields.

When building a list interface, create instances of this class and use them to populate your [`CPListImageRowItem`](./cplistimagerowitem.md) type. To handle row-related interactions with elements in a row, configure the [`listImageRowHandler`](./cplistimagerowitem/listimagerowhandler.md) property of the row itself.

## Topics

### Creating a row element
- [init(image: UIImage, title: String?, subtitle: String?)](./cplistimagerowitemrowelement/init%28image,title,subtitle%29.md)
  Creates a row element with the specified image and optional text.
### Getting the element’s content
- [var title: String?](./cplistimagerowitemrowelement/title.md)
  The primary text for the element.
- [var subtitle: String?](./cplistimagerowitemrowelement/subtitle.md)
  The secondary text for the element.

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
- [class CPListImageRowItemCardElement](./cplistimagerowitemcardelement.md)
  A row element that displays an image and text on a card-style background.
- [class CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
  A row element that displays an image and text in a vertically condensed style.
- [class CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
  A row element that displays an image.
- [class CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
  A row element that displays an image with a custom cutout shape and a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemrowelement)*