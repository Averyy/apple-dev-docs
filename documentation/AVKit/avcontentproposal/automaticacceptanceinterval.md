# automaticAcceptanceInterval

**Framework**: AVKit  
**Kind**: property

The interval between the time playback ends and automatic acceptance of this content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var automaticAcceptanceInterval: TimeInterval { get set }
```

#### Discussion

The content proposal displays a countdown timer to reflect this value. Set this value to [`nan`](https://developer.apple.com/documentation/Swift/Double/nan) to disable the default, which is automatic acceptance.

## See Also

- [var contentTimeForTransition: CMTime](avcontentproposal/contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](avcontentproposal/title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](avcontentproposal/previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](avcontentproposal/metadata.md)
  Optional custom metadata associated with the proposed item.
- [var url: URL?](avcontentproposal/url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/automaticacceptanceinterval)*