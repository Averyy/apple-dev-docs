# previewVideoURL

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The URL for the content’s trailer or preview.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var previewVideoURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * previewVideoURL;
```

#### Discussion

When the navigation focus stops on the item, the system removes the item’s static image or cinemagraph video and plays the video at the specified URL.

## See Also

### Specifying the Content Previews
- [var cinemagraphURL: URL?](./cinemagraphurl.md)
  The URL of a looping video to play, without sound, while the preview loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/previewvideourl)*