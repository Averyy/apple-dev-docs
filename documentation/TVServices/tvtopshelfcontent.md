# TVTopShelfContent

**Framework**: TV Services  
**Kind**: protocol

The protocol that objects adopt to provide content for the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVTopShelfContent : NSObjectProtocol
```

#### Overview

Don’t adopt this protocol in your own classes. The TVServices framework adopts this protocol in classes that can contain top shelf content, such as the [`TVTopShelfCarouselContent`](tvtopshelfcarouselcontent.md) class.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [TVTopShelfCarouselContent](tvtopshelfcarouselcontent.md)
- [TVTopShelfInsetContent](tvtopshelfinsetcontent.md)
- [TVTopShelfSectionedContent](tvtopshelfsectionedcontent.md)

## See Also

- [class TVTopShelfItem](tvtopshelfitem.md)
  An item that uses an image to represent a movie, show, or other content in the top shelf.
- [class TVTopShelfAction](tvtopshelfaction.md)
  An action to perform in response to user interactions with an item in the top shelf.
- [class TVTopShelfObject](tvtopshelfobject.md)
  An abstract base class for describing top shelf items and item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontent)*