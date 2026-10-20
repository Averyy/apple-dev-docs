# creationDate

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The date when the content item was created, or the date when it was first broadcast, or some other kind of origination date.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var creationDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * creationDate;
```

## See Also

### Inspecting the Content Properties
- [var duration: NSNumber?](./duration.md)
  The amount of time required to play the media to completion.
- [var expirationDate: Date?](./expirationdate.md)
  The date when the user will no longer be able to access the item.
- [var imageShape: TVContentItemImageShape](./imageshape.md)
  The intended aspect ratio or shape of the content image.
- [enum TVContentItemImageShape](../tvcontentitemimageshape.md)
  An enumerated type that identifies the shape in which the content item should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/creationdate)*