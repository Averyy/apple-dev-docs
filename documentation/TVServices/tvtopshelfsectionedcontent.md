# TVTopShelfSectionedContent

**Framework**: TV Services  
**Kind**: class  
**Role**: Class

The set of items you want to present using a section-based interface in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfSectionedContent
```

```objc
@interface TVTopShelfSectionedContent : NSObject
```

#### Overview

Create a [`TVTopShelfSectionedContent`](./tvtopshelfsectionedcontent.md) object when you want to display your top shelf content using a sectioned interface. A sectioned interface displays a single labled row of items. Items are organized by section. As the row scrolls horizontally through the items, the system updates the label above the items to indicate the current section. You specify the title of each section and its items using [`TVTopShelfItemCollection`](./tvtopshelfitemcollection.md) objects.

For more information about how to configure images for a sectioned interface, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/tvos/icons-and-images/top-shelf-images/).

## Topics

### Creating a Sectioned Content Object
- [init(sections: [TVTopShelfItemCollection<TVTopShelfSectionedItem>])](./tvtopshelfsectionedcontent/init%28sections%29.md)
  Creates a sectioned content object and populates it with the specified sections.
### Getting the Sections
- [var sections: [TVTopShelfItemCollection<TVTopShelfSectionedItem>]](./tvtopshelfsectionedcontent/sections.md)
  The sections to display in the interface.
### Getting the Image Size Information
- [class func imageSize(for: TVTopShelfSectionedItem.ImageShape) -> CGSize](./tvtopshelfsectionedcontent/imagesize%28for%29.md)
  Returns the dimensions to use for images of the specified shape.
- [TVTopShelfSectionedItem.ImageShape](./tvtopshelfsectioneditem/imageshape-swift.enum.md)
  Constants indicating the aspect ratio of an image.

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

### Sectioned and inset content
- [class TVTopShelfSectionedItem](./tvtopshelfsectioneditem.md)
  An item to display in a section-based interface.
- [class TVTopShelfItemCollection](./tvtopshelfitemcollection.md)
  A group of items that you display together in a sectioned interface in the top shelf.
- [class TVTopShelfInsetContent](./tvtopshelfinsetcontent.md)
  A set of items to present using an inset-style interface in the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectionedcontent)*