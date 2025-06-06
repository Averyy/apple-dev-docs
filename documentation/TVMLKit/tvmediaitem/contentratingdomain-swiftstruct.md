# TVMediaItem.ContentRatingDomain

**Framework**: TVMLKit  
**Kind**: struct

A value identifying the media’s content rating domain.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
struct ContentRatingDomain
```

## Topics

### Rating Domains
- [static let movie: TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct/movie.md)
  The media item’s rating uses the movie domain.
- [static let music: TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct/music.md)
  The media item’s rating uses the music domain.
- [static let tvShow: TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct/tvshow.md)
  The media item’s rating uses the TV show domain.
### Initializers
- [init(String)](tvmediaitem/contentratingdomain-swift.struct/init(_:).md)
- [init(rawValue: String)](tvmediaitem/contentratingdomain-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var containsExplicitContent: Bool](tvmediaitem/containsexplicitcontent.md)
  A Boolean value indicating whether the item contains adult-oriented content.
- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](tvmediaitem/contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [var contentRatingRanking: NSNumber?](tvmediaitem/contentratingranking.md)
  The rating for a video item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/contentratingdomain-swift.struct)*