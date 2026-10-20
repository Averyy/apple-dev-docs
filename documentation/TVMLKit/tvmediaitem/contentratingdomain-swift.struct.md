# TVMediaItem.ContentRatingDomain

**Framework**: TVMLKit  
**Kind**: struct  
**Role**: Structure

A value identifying the media’s content rating domain.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
struct ContentRatingDomain
```

```c
typedef NSString * TVMediaItemContentRatingDomain;
```

## Topics

### Rating Domains
- [static let movie: TVMediaItem.ContentRatingDomain](./contentratingdomain-swift.struct/movie.md)
  The media item’s rating uses the movie domain.
- [static let music: TVMediaItem.ContentRatingDomain](./contentratingdomain-swift.struct/music.md)
  The media item’s rating uses the music domain.
- [static let tvShow: TVMediaItem.ContentRatingDomain](./contentratingdomain-swift.struct/tvshow.md)
  The media item’s rating uses the TV show domain.
### Initializers
- [init(String)](./contentratingdomain-swift.struct/init%28_%29.md)
- [init(rawValue: String)](./contentratingdomain-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Rating Media Content
- [var containsExplicitContent: Bool](./containsexplicitcontent.md)
  A Boolean value indicating whether the item contains adult-oriented content.
- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](./contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [var contentRatingRanking: NSNumber?](./contentratingranking.md)
  The rating for a video item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/contentratingdomain-swift.struct)*