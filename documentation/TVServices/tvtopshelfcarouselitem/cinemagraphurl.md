# cinemagraphURL

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The URL of a looping video to play, without sound, while the preview loads.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var cinemagraphURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * cinemagraphURL;
```

#### Discussion

If you specify a value for this property, the system initially displays the corresponding video instead of a static image. The video plays in a loop until the preview video loads and is ready to play. If you do not specify a value for this property, the system displays the image you set using the [`setImageURL(_:for:)`](../tvtopshelfitem/setimageurl%28_,for%29.md) method.

The system does not play any sound content present in the video, so there is no need to include it when creating your assets.

## See Also

### Specifying the Content Previews
- [var previewVideoURL: URL?](./previewvideourl.md)
  The URL for the content’s trailer or preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/cinemagraphurl)*