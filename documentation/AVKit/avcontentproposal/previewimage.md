# previewImage

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The preview image of the proposed item.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var previewImage: UIImage? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIImage * previewImage;
```

#### Discussion

The preview image you provide should typically be a frame from the proposed video, not the poster artwork.

## See Also

### Configuring the content proposal
- [var contentTimeForTransition: CMTime](./contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](./title.md)
  The title of the proposed content.
- [var metadata: [AVMetadataItem]](./metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](./automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](./url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/previewimage)*