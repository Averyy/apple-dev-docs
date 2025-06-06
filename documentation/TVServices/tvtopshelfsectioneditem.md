# TVTopShelfSectionedItem

**Framework**: TV Services  
**Kind**: class

An item to display in a section-based interface.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfSectionedItem
```

#### Overview

Create a [`TVTopShelfSectionedItem`](tvtopshelfsectioneditem.md) object for each item you want to display in the top shelf. Each sectioned item corresponds to one item of your app’s content. For example, a video playback app uses sectioned items to represent movies or shows. Specify the image for the item using the [`setImageURL(_:for:)`](tvtopshelfitem/setimageurl(_:for:).md) method. Use the inherited [`playAction`](tvtopshelfitem/playaction.md) and [`displayAction`](tvtopshelfitem/displayaction.md) properties to let the system know what to do when the user interacts with the item.

## Topics

### Setting the Image Shape
- [var imageShape: TVTopShelfSectionedItem.ImageShape](tvtopshelfsectioneditem/imageshape-swift.property.md)
  The aspect ratio of the item’s image.
- [TVTopShelfSectionedItem.ImageShape](tvtopshelfsectioneditem/imageshape-swift.enum.md)
  Constants indicating the aspect ratio of an image.
### Setting the Playback Progress
- [var playbackProgress: Double](tvtopshelfsectioneditem/playbackprogress.md)
  The percentage of the content that the user has already played, specified as a value between 0.0 and 1.0.

## Relationships

### Inherits From
- [TVTopShelfItem](tvtopshelfitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVTopShelfItemCollection](tvtopshelfitemcollection.md)
  A group of items that you display together in a sectioned interface in the top shelf.
- [class TVTopShelfSectionedContent](tvtopshelfsectionedcontent.md)
  The set of items you want to present using a section-based interface in the top shelf.
- [class TVTopShelfInsetContent](tvtopshelfinsetcontent.md)
  A set of items to present using an inset-style interface in the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectioneditem)*