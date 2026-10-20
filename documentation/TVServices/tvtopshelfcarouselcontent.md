# TVTopShelfCarouselContent

**Framework**: TV Services  
**Kind**: class  
**Role**: Class

A set of items you present using a carousel-style interface in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfCarouselContent
```

```objc
@interface TVTopShelfCarouselContent : NSObject
```

## Topics

### Creating a Carousel Content Object
- [init(style: TVTopShelfCarouselContent.Style, items: [TVTopShelfCarouselItem])](./tvtopshelfcarouselcontent/init%28style,items%29.md)
  Creates a content object for displaying items in a carousel style in the top shelf interface.
### Accessing the Carousel Items
- [var items: [TVTopShelfCarouselItem]](./tvtopshelfcarouselcontent/items.md)
  The items to display in the top shelf interface.
### Getting the Item Style
- [var style: TVTopShelfCarouselContent.Style](./tvtopshelfcarouselcontent/style-swift.property.md)
  The appearance to use when displaying items in the top shelf interface.
- [TVTopShelfCarouselContent.Style](./tvtopshelfcarouselcontent/style-swift.enum.md)
  Constants indicating how you want items to appear in the top shelf interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [TVTopShelfContent](./tvtopshelfcontent.md)

## See Also

### Carousel content
- [class TVTopShelfCarouselItem](./tvtopshelfcarouselitem.md)
  An item containing images, video, and other information that you want to display using a carousel-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselcontent)*