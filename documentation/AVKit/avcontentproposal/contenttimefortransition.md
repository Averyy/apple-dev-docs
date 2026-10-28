# contentTimeForTransition

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The time within the timeline of the current player item when the content proposal presentation should begin.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var contentTimeForTransition: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime contentTimeForTransition;
```

## Discussion

The time value commonly marks the beginning of the end credits in a television show or movie. For other content, this may be at the very end of the video. The default value, [`indefinite`](../../CoreMedia/cmtime/indefinite.md), indicates that the transition should occur at the very end of the current player item’s end time; this is equivalent to using the duration of the asset.

## See Also

### Configuring the content proposal
- [var title: String](./title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](./previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](./metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](./automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](./url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/contenttimefortransition)*