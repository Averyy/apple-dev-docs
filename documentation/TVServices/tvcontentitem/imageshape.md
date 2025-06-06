# imageShape

**Framework**: TV Services  
**Kind**: property

The intended aspect ratio or shape of the content image.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var imageShape: TVContentItemImageShape { get set }
```

#### Discussion

When the TV Content object is being used to represent Top Shelf items, then the allowed values for this property depend on the [`topShelfStyle`](tvtopshelfprovider/topshelfstyle.md) property of the object that implements the TV TopShelf extension. For more information, see [`TVTopShelfProvider`](tvtopshelfprovider.md).

If the [`topShelfStyle`](tvtopshelfprovider/topshelfstyle.md) value is [`TVTopShelfContentStyle.inset`](tvtopshelfcontentstyle/inset.md), the valid values of this property are:

- [`TVContentItemImageShape.extraWide`](tvcontentitemimageshape/extrawide.md)

If the [`topShelfStyle`](tvtopshelfprovider/topshelfstyle.md) value is [`TVTopShelfContentStyle.sectioned`](tvtopshelfcontentstyle/sectioned.md), the valid values are:

- [`TVContentItemImageShape.poster`](tvcontentitemimageshape/poster.md)
- [`TVContentItemImageShape.square`](tvcontentitemimageshape/square.md)
- [`TVContentItemImageShape.HDTV`](tvcontentitemimageshape/hdtv.md)

If the value of this property is not valid for the current Top Shelf style, the system reserves the right to scale the image in any way.

## See Also

- [var creationDate: Date?](tvcontentitem/creationdate.md)
  The date when the content item was created, or the date when it was first broadcast, or some other kind of origination date.
- [var duration: NSNumber?](tvcontentitem/duration.md)
  The amount of time required to play the media to completion.
- [var expirationDate: Date?](tvcontentitem/expirationdate.md)
  The date when the user will no longer be able to access the item.
- [enum TVContentItemImageShape](tvcontentitemimageshape.md)
  An enumerated type that identifies the shape in which the content item should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/imageshape)*