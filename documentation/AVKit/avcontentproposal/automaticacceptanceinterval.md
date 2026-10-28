# automaticAcceptanceInterval

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The interval between the time playback ends and automatic acceptance of this content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var automaticAcceptanceInterval: TimeInterval { get set }
```

```objc
@property (nonatomic, readwrite) NSTimeInterval automaticAcceptanceInterval;
```

## Discussion

The content proposal displays a countdown timer to reflect this value. Set this value to [`nan`](../../Swift/double/nan.md) to disable the default, which is automatic acceptance.

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
- [var url: URL?](./url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/automaticacceptanceinterval)*