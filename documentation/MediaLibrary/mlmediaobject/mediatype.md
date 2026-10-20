# mediaType

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The media object’s type of media (image, audio, or movie).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var mediaType: MLMediaType { get }
```

```objc
@property (assign, readonly) MLMediaType mediaType;
```

#### Discussion

For a list of possible media types, see [`MLMediaType`](../mlmediatype.md).

## See Also

### Accessing Object Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media object.
- [var contentType: String?](./contenttype.md)
  The UTI associated with the media object.
- [var name: String?](./name.md)
  The name of the media object.
- [var url: URL?](./url.md)
  The location of the media object.
- [var originalURL: URL?](./originalurl.md)
  The location of the original media object, if [`url`](./url.md) is not the original location.
- [var fileSize: Int](./filesize.md)
  The size, in bytes, of the media object.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media object was last altered.
- [var thumbnailURL: URL?](./thumbnailurl.md)
  The location of the media object’s thumbnail image.
- [var artworkImage: NSImage?](./artworkimage.md)
  Album artwork associated with the media object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobject/mediatype)*