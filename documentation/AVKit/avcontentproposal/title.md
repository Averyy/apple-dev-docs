# title

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The title of the proposed content.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * title;
```

## See Also

### Configuring the content proposal
- [var contentTimeForTransition: CMTime](./contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var previewImage: UIImage?](./previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](./metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](./automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](./url.md)
  The URL of the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/title)*