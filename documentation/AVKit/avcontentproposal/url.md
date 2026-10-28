# url

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The URL of the proposed content.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var url: URL? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) NSURL * URL;
```

## Discussion

Use this property value to initialize a new [`AVPlayerItem`](../../AVFoundation/avplayeritem.md) to play when the user accepts the content proposal. If the value of this property is `nil`, the [`AVPlayerViewControllerDelegate`](../avplayerviewcontrollerdelegate.md) must handle the content proposal acceptance.

## See Also

### Configuring the content proposal
- [var contentTimeForTransition: CMTime](./contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](./title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](./previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](./metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](./automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/url)*