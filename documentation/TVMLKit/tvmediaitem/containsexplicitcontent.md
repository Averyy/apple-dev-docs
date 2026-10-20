# containsExplicitContent

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the item contains adult-oriented content.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var containsExplicitContent: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL containsExplicitContent;
```

#### Discussion

This property is ignored when the [`type`](./type.md) is `video`.

## See Also

### Rating Media Content
- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](./contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [TVMediaItem.ContentRatingDomain](./contentratingdomain-swift.struct.md)
  A value identifying the media’s content rating domain.
- [var contentRatingRanking: NSNumber?](./contentratingranking.md)
  The rating for a video item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/containsexplicitcontent)*