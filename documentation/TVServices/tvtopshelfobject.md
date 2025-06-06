# TVTopShelfObject

**Framework**: TV Services  
**Kind**: class

An abstract base class for describing top shelf items and item collections.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfObject
```

#### Overview

This class provides shared information for objects you use in your app extension. Do not create instances of this class directly.

## Topics

### Getting the Object Attributes
- [var title: String?](tvtopshelfobject/title.md)
  The localized title of the object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TVTopShelfItem](tvtopshelfitem.md)
- [TVTopShelfItemCollection](tvtopshelfitemcollection.md)
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
- [class TVTopShelfAction](tvtopshelfaction.md)
  An action to perform in response to user interactions with an item in the top shelf.
- [protocol TVTopShelfContent](tvtopshelfcontent.md)
  The protocol that objects adopt to provide content for the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfobject)*