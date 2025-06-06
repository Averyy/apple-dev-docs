# name

**Framework**: Media Library  
**Kind**: property

The name of the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var name: String? { get }
```

#### Discussion

This string is human-readable. It is either user created (such as the name of an iTunes playlist) or already localized.

## See Also

- [var attributes: [String : Any]](mlmediagroup/attributes.md)
  A dictionary of attributes describing the media group.
- [var iconImage: NSImage?](mlmediagroup/iconimage.md)
  The media group’s icon.
- [var url: URL?](mlmediagroup/url.md)
  The location of the media group.
- [var modificationDate: Date?](mlmediagroup/modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/name)*