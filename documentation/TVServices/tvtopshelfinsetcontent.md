# TVTopShelfInsetContent

**Framework**: TV Services  
**Kind**: class

A set of items to present using an inset-style interface in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfInsetContent
```

#### Overview

Create a [`TVTopShelfInsetContent`](tvtopshelfinsetcontent.md) object when you want to display your top shelf content using an inset interface. The layout for an inset interface shows a series of large images, each of which spans almost the entire width of the screen. The focused image appears raised above the background.

For more information about how to configure images for an inset interface, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/tvos/icons-and-images/top-shelf-images/).

## Topics

### Creating an Inset Content Object
- [init(items: [TVTopShelfItem])](tvtopshelfinsetcontent/init(items:).md)
  Creates an inset content object and populates it with the specified set of items.
### Getting the Items
- [var items: [TVTopShelfItem]](tvtopshelfinsetcontent/items.md)
  The items to display from the inset interface.
### Getting the Image Size
- [class var imageSize: CGSize](tvtopshelfinsetcontent/imagesize.md)
  The standard width and height for images in an inset interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TVTopShelfContent](tvtopshelfcontent.md)

## See Also

- [class TVTopShelfSectionedItem](tvtopshelfsectioneditem.md)
  An item to display in a section-based interface.
- [class TVTopShelfItemCollection](tvtopshelfitemcollection.md)
  A group of items that you display together in a sectioned interface in the top shelf.
- [class TVTopShelfSectionedContent](tvtopshelfsectionedcontent.md)
  The set of items you want to present using a section-based interface in the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfinsetcontent)*