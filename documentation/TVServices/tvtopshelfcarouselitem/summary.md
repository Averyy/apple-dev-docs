# summary

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

A descriptive summary of a movie or show.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var summary: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * summary;
```

#### Discussion

The system displays the summary only in the [`TVTopShelfCarouselContent.Style.details`](../tvtopshelfcarouselcontent/style-swift.enum/details.md) style.

## See Also

### Specifying the Item Details
- [var contextTitle: String?](./contexttitle.md)
  A localized string describing why the item is shown in the top shelf.
- [var genre: String?](./genre.md)
  The genre assigned to the movie or show.
- [var duration: TimeInterval](./duration.md)
  The length of the movie or show, in seconds.
- [var creationDate: Date?](./creationdate.md)
  The original release date of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/summary)*