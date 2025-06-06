# TVTopShelfItem

**Framework**: TV Services  
**Kind**: class

An item that uses an image to represent a movie, show, or other content in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfItem
```

#### Overview

A [`TVTopShelfItem`](tvtopshelfitem.md) object manages basic traits for all items, including the images they display and the actions they trigger. Typically, you create [`TVTopShelfCarouselItem`](tvtopshelfcarouselitem.md) or [`TVTopShelfSectionedItem`](tvtopshelfsectioneditem.md) objects for your interface. For inset interfaces, you can also create [`TVTopShelfItem`](tvtopshelfitem.md) objects directly.

After creating an item object, assign an image and one or more actions to it, and update any other relevant properties. Return the item object as part of the content for your interface.

Each unique item in your app must have a correspondingly unique identifier, and the identifier for each item must remain stable throughout the life of your app. Do not assign a different unique identifier for the same underlying item each time you create a [`TVTopShelfItem`](tvtopshelfitem.md) object for it.

## Topics

### Creating a Top Shelf Item
- [init(identifier: String)](tvtopshelfitem/init(identifier:).md)
  Creates a top shelf item with the specified identifier.
### Assigning Actions to the Item
- [var playAction: TVTopShelfAction?](tvtopshelfitem/playaction.md)
  The action to perform when the user wants to play the current item.
- [var displayAction: TVTopShelfAction?](tvtopshelfitem/displayaction.md)
  The action to perform when the user wants to see more information for the current item.
### Providing an Image for the Item
- [func imageURL(for: TVTopShelfItem.ImageTraits) -> URL?](tvtopshelfitem/imageurl(for:).md)
  Returns an image associated with the current item.
- [func setImageURL(URL?, for: TVTopShelfItem.ImageTraits)](tvtopshelfitem/setimageurl(_:for:).md)
  Associates an image with the current item.
- [TVTopShelfItem.ImageTraits](tvtopshelfitem/imagetraits.md)
  Constants describing the image format.
### Getting the Item Attributes
- [var identifier: String](tvtopshelfitem/identifier.md)
  The unique identifier for the item.
- [var expirationDate: Date?](tvtopshelfitem/expirationdate.md)
  The date on which the item becomes unavailable.

## Relationships

### Inherits From
- [TVTopShelfObject](tvtopshelfobject.md)
### Inherited By
- [TVTopShelfCarouselItem](tvtopshelfcarouselitem.md)
- [TVTopShelfSectionedItem](tvtopshelfsectioneditem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVTopShelfAction](tvtopshelfaction.md)
  An action to perform in response to user interactions with an item in the top shelf.
- [protocol TVTopShelfContent](tvtopshelfcontent.md)
  The protocol that objects adopt to provide content for the top shelf.
- [class TVTopShelfObject](tvtopshelfobject.md)
  An abstract base class for describing top shelf items and item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem)*