# originalURL

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The location of the original media object, if [`url`](./url.md) is not the original location.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var originalURL: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * originalURL;
```

#### Discussion

This property is provided as a security-scoped URL. In order to gain access to the file that this URL refers to, the caller must call [`startAccessingSecurityScopedResource()`](../../Foundation/nsurl/startaccessingsecurityscopedresource%28%29.md) before and [`stopAccessingSecurityScopedResource()`](../../Foundation/nsurl/stopaccessingsecurityscopedresource%28%29.md) after using the URL to access the file. For more information about security-scoped URLs, see [`NSURL`](../../Foundation/nsurl.md).

## See Also

### Accessing Object Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media object.
- [var mediaType: MLMediaType](./mediatype.md)
  The media object’s type of media (image, audio, or movie).
- [var contentType: String?](./contenttype.md)
  The UTI associated with the media object.
- [var name: String?](./name.md)
  The name of the media object.
- [var url: URL?](./url.md)
  The location of the media object.
- [var fileSize: Int](./filesize.md)
  The size, in bytes, of the media object.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media object was last altered.
- [var thumbnailURL: URL?](./thumbnailurl.md)
  The location of the media object’s thumbnail image.
- [var artworkImage: NSImage?](./artworkimage.md)
  Album artwork associated with the media object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobject/originalurl)*