# thumbnailURL

**Framework**: Media Library  
**Kind**: property

The location of the media object’s thumbnail image.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var thumbnailURL: URL? { get }
```

#### Discussion

This property is provided as a security-scoped URL. In order to gain access to the file that this URL refers to, the caller must call [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) before and [`stopAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou) after using the URL to access the file. For more information about security-scoped URLs, see [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL).

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
- [var fileSize: Int](mlmediaobject/filesize.md)
  The size, in bytes, of the media object.
- [var modificationDate: Date?](mlmediaobject/modificationdate.md)
  The date and time when the media object was last altered.
- [var artworkImage: NSImage?](mlmediaobject/artworkimage.md)
  Album artwork associated with the media object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobject/thumbnailurl)*