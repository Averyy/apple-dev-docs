# url

**Framework**: AVKit  
**Kind**: property

The URL of the proposed content.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var url: URL? { get set }
```

#### Discussion

Use this property value to initialize a new [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) to play when the user accepts the content proposal. If the value of this property is `nil`, the [`AVPlayerViewControllerDelegate`](avplayerviewcontrollerdelegate.md) must handle the content proposal acceptance.

## See Also

- [var contentTimeForTransition: CMTime](avcontentproposal/contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](avcontentproposal/title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](avcontentproposal/previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](avcontentproposal/metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](avcontentproposal/automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/url)*