# TVContentItemImageShape

**Framework**: TV Services  
**Kind**: enum

An enumerated type that identifies the shape in which the content item should be displayed.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum TVContentItemImageShape
```

## Topics

### Constants
- [TVContentItemImageShape.none](tvcontentitemimageshape/none.md)
  The content has no particular shape.
- [TVContentItemImageShape.poster](tvcontentitemimageshape/poster.md)
  The content has a width:height ratio of `2:3`.
- [TVContentItemImageShape.square](tvcontentitemimageshape/square.md)
  The content has a width:height ratio of `1:1`.
- [TVContentItemImageShape.SDTV](tvcontentitemimageshape/sdtv.md)
  The content is standard-definition television content with a width:height ratio of `4:3`.
- [TVContentItemImageShape.HDTV](tvcontentitemimageshape/hdtv.md)
  The content is high-definition television content with a width:height ratio of `16:9`.
- [TVContentItemImageShape.wide](tvcontentitemimageshape/wide.md)
  The content has a width:height ratio of `8:3`.
- [TVContentItemImageShape.extraWide](tvcontentitemimageshape/extrawide.md)
  The content has a width:height ratio of `80:27`.
### Initializers
- [init?(rawValue: Int)](tvcontentitemimageshape/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var creationDate: Date?](tvcontentitem/creationdate.md)
  The date when the content item was created, or the date when it was first broadcast, or some other kind of origination date.
- [var duration: NSNumber?](tvcontentitem/duration.md)
  The amount of time required to play the media to completion.
- [var expirationDate: Date?](tvcontentitem/expirationdate.md)
  The date when the user will no longer be able to access the item.
- [var imageShape: TVContentItemImageShape](tvcontentitem/imageshape.md)
  The intended aspect ratio or shape of the content image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape)*