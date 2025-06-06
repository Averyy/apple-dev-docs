# fileSize

**Framework**: Media Library  
**Kind**: property

The size, in bytes, of the media object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var fileSize: Int { get }
```

## See Also

- [var attributes: [String : Any]](mlmediaobject/attributes.md)
  A dictionary of attributes describing the media object.
- [var mediaType: MLMediaType](mlmediaobject/mediatype.md)
  The media object’s type of media (image, audio, or movie).
- [var contentType: String?](mlmediaobject/contenttype.md)
  The UTI associated with the media object.
- [var name: String?](mlmediaobject/name.md)
  The name of the media object.
- [var url: URL?](mlmediaobject/url.md)
  The location of the media object.
- [var originalURL: URL?](mlmediaobject/originalurl.md)
  The location of the original media object, if [`url`](mlmediaobject/url.md) is not the original location.
- [var modificationDate: Date?](mlmediaobject/modificationdate.md)
  The date and time when the media object was last altered.
- [var thumbnailURL: URL?](mlmediaobject/thumbnailurl.md)
  The location of the media object’s thumbnail image.
- [var artworkImage: NSImage?](mlmediaobject/artworkimage.md)
  Album artwork associated with the media object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobject/filesize)*