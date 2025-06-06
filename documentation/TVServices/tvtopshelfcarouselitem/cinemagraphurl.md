# cinemagraphURL

**Framework**: TV Services  
**Kind**: property

The URL of a looping video to play, without sound, while the preview loads.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var cinemagraphURL: URL? { get set }
```

#### Discussion

If you specify a value for this property, the system initially displays the corresponding video instead of a static image. The video plays in a loop until the preview video loads and is ready to play. If you do not specify a value for this property, the system displays the image you set using the [`setImageURL(_:for:)`](tvtopshelfitem/setimageurl(_:for:).md) method.

The system does not play any sound content present in the video, so there is no need to include it when creating your assets.

## See Also

- [var previewVideoURL: URL?](tvtopshelfcarouselitem/previewvideourl.md)
  The URL for the content’s trailer or preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/cinemagraphurl)*