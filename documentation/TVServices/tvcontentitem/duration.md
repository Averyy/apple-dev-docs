# duration

**Framework**: TV Services  
**Kind**: property

The amount of time required to play the media to completion.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@NSCopying
var duration: NSNumber? { get set }
```

#### Discussion

The duration number is interpreted as a double number of seconds.

## See Also

- [var creationDate: Date?](tvcontentitem/creationdate.md)
  The date when the content item was created, or the date when it was first broadcast, or some other kind of origination date.
- [var expirationDate: Date?](tvcontentitem/expirationdate.md)
  The date when the user will no longer be able to access the item.
- [var imageShape: TVContentItemImageShape](tvcontentitem/imageshape.md)
  The intended aspect ratio or shape of the content image.
- [enum TVContentItemImageShape](tvcontentitemimageshape.md)
  An enumerated type that identifies the shape in which the content item should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/duration)*