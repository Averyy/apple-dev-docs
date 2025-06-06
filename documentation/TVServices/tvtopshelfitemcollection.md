# TVTopShelfItemCollection

**Framework**: TV Services  
**Kind**: class

A group of items that you display together in a sectioned interface in the top shelf.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfItemCollection<Item> where Item : TVTopShelfItem
```

#### Overview

Use a [`TVTopShelfItemCollection`](tvtopshelfitemcollection.md) object to organize related groups of items in a sectioned interface. The system presents the items in your collection together, displaying the [`title`](tvtopshelfobject/title.md) of the collection above those items. For example, you might create different collections for new movies, the user’s favorites, and recently watched movies.

## Topics

### Creating an Item Collection
- [init(items: [Item])](tvtopshelfitemcollection/init(items:).md)
  Creates an item collection object from the specified set of top shelf items.
### Getting the Items
- [var items: [Item]](tvtopshelfitemcollection/items.md)
  The items in the collection.

## Relationships

### Inherits From
- [TVTopShelfObject](tvtopshelfobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVTopShelfSectionedItem](tvtopshelfsectioneditem.md)
  An item to display in a section-based interface.
- [class TVTopShelfSectionedContent](tvtopshelfsectionedcontent.md)
  The set of items you want to present using a section-based interface in the top shelf.
- [class TVTopShelfInsetContent](tvtopshelfinsetcontent.md)
  A set of items to present using an inset-style interface in the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitemcollection)*