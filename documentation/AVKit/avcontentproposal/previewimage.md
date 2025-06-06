# previewImage

**Framework**: AVKit  
**Kind**: property

The preview image of the proposed item.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var previewImage: UIImage? { get }
```

#### Discussion

The preview image you provide should typically be a frame from the proposed video, not the poster artwork.

## See Also

- [var contentTimeForTransition: CMTime](avcontentproposal/contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](avcontentproposal/title.md)
  The title of the proposed content.
- [var metadata: [AVMetadataItem]](avcontentproposal/metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](avcontentproposal/automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](avcontentproposal/url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/previewimage)*