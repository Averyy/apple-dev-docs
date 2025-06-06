# containsExplicitContent

**Framework**: TVMLKit  
**Kind**: property

A Boolean value indicating whether the item contains adult-oriented content.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var containsExplicitContent: Bool { get }
```

#### Discussion

This property is ignored when the [`type`](tvmediaitem/type.md) is `video`.

## See Also

- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](tvmediaitem/contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct.md)
  A value identifying the media’s content rating domain.
- [var contentRatingRanking: NSNumber?](tvmediaitem/contentratingranking.md)
  The rating for a video item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/containsexplicitcontent)*