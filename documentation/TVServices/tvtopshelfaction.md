# TVTopShelfAction

**Framework**: TV Services  
**Kind**: class

An action to perform in response to user interactions with an item in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfAction
```

#### Overview

A [`TVTopShelfAction`](tvtopshelfaction.md) object contains the URL that you want tvOS to open when the user selects an item in the top shelf. Use actions to specify the location of playable content or pages containing additional information.

When configuring a [`TVTopShelfItem`](tvtopshelfitem.md) to display in a carousel interface, the system chooses a title and image for each button on the item based on whether you assigned the action object to the [`playAction`](tvtopshelfitem/playaction.md) or [`displayAction`](tvtopshelfitem/displayaction.md) property of your item.

## Topics

### Creating an Action Object
- [init(url: URL)](tvtopshelfaction/init(url:).md)
  Creates a new action object that displays the content at the specified URL.
### Getting the URL
- [var url: URL](tvtopshelfaction/url.md)
  The URL of the content you want to display.

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

## See Also

- [class TVTopShelfItem](tvtopshelfitem.md)
  An item that uses an image to represent a movie, show, or other content in the top shelf.
- [protocol TVTopShelfContent](tvtopshelfcontent.md)
  The protocol that objects adopt to provide content for the top shelf.
- [class TVTopShelfObject](tvtopshelfobject.md)
  An abstract base class for describing top shelf items and item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfaction)*