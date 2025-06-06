# contentRatingRanking

**Framework**: TVMLKit  
**Kind**: property

The rating for a video item.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var contentRatingRanking: NSNumber? { get }
```

#### Discussion

The rating is a value from `0-1000`. This value corresponds to a specific rating used by different countries. For example, a rating value can represent a PG-13 rating in the United States and an MA15+ in Australia.

## See Also

- [var containsExplicitContent: Bool](tvmediaitem/containsexplicitcontent.md)
  A Boolean value indicating whether the item contains adult-oriented content.
- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](tvmediaitem/contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct.md)
  A value identifying the media’s content rating domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/contentratingranking)*