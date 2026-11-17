# CPListImageRowItemCardElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row element that displays an image and text on a card-style background.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemCardElement
```

```objc
@interface CPListImageRowItemCardElement : CPListImageRowItemElement
```

## Overview

The `CPListImageRowItemCardElement ` class defines an element you add to a row in a list template. Use this class with the [`CPListImageRowItem`](./cplistimagerowitem.md) type to place multiple items in each row of your list. This element type displays a required image and an optional title and subtitle on top of a tinted background with a card shape. When possible, provide text values with meaningful information. For example, an element displaying the artwork for an album might display the album’s name and band information in the text fields.

When building a list interface, create instances of this class and use them to populate your [`CPListImageRowItem`](./cplistimagerowitem.md) type. When configuring elements using a thumbnail image, the aspect ratio of the first image defines the layout of the remaining elements. To handle row-related interactions with elements in a row, configure the [`listImageRowHandler`](./cplistimagerowitem/listimagerowhandler.md) property of the row itself.

## Topics

### Creating a card element
- [init(image: UIImage, showsImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)](./cplistimagerowitemcardelement/init%28image,showsimagefullheight,title,subtitle,tintcolor%29.md)
  Creates a card row element with the specified image, text, and card background color.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, tintColor: UIColor?)](./cplistimagerowitemcardelement/init%28thumbnail,title,subtitle,tintcolor%29.md)
  Creates a card row element with a thumbnail image, text, and background color.
- [init?(coder: NSCoder)](./cplistimagerowitemcardelement/init%28coder%29.md)
### Getting the element’s content
- [var title: String](./cplistimagerowitemcardelement/title.md)
  The primary text for the element.
- [var subtitle: String?](./cplistimagerowitemcardelement/subtitle.md)
  The secondary text for the element.
- [var tintColor: UIColor?](./cplistimagerowitemcardelement/tintcolor.md)
  The color to use for the card’s background.
### Getting the image behavior
- [var thumbnail: CPThumbnailImage?](./cplistimagerowitemcardelement/thumbnail.md)
  The thumbnail object that provides the image content.
- [var showsImageFullHeight: Bool](./cplistimagerowitemcardelement/showsimagefullheight.md)
  A Boolean value that indicates whether to use a full-height image for the card.
### Getting the expected image dimensions
- [class var maximumFullHeightImageSize: CGSize](./cplistimagerowitemcardelement/maximumfullheightimagesize.md)
  The maximum dimensions for full-height images.
- [class var maximumImageSize: CGSize](./cplistimagerowitemcardelement/maximumimagesize.md)
  The maximum dimensions for normal-height images.

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
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Row elements
- [class CPListImageRowItemRowElement](./cplistimagerowitemrowelement.md)
  A row element that displays an image, title, and subtitle.
- [class CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
  A row element that displays an image and text in a vertically condensed style.
- [class CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
  A row element that displays an image.
- [class CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
  A row element that displays an image with a custom cutout shape and a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement)*