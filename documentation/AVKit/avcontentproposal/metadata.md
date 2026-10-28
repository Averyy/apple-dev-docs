# metadata

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Optional custom metadata associated with the proposed item.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVMetadataItem *> * metadata;
```

## Discussion

In addition to the title and preview image, you can associate any custom metadata you need for the presentation of this content proposal.

## See Also

### Configuring the content proposal
- [var contentTimeForTransition: CMTime](./contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](./title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](./previewimage.md)
  The preview image of the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](./automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](./url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/metadata)*