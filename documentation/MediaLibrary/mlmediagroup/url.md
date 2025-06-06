# url

**Framework**: Media Library  
**Kind**: property

The location of the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

Some groups do not have a URL, in which case this returns `nil`. For example, a group that represents a filesystem folder on disk has a URL, but a group that represents a named face in iPhoto does not.

## See Also

- [var attributes: [String : Any]](mlmediagroup/attributes.md)
  A dictionary of attributes describing the media group.
- [var name: String?](mlmediagroup/name.md)
  The name of the media group.
- [var iconImage: NSImage?](mlmediagroup/iconimage.md)
  The media group’s icon.
- [var modificationDate: Date?](mlmediagroup/modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/url)*