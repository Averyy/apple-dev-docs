# iconImage

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The media group’s icon.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
@NSCopying
var iconImage: NSImage? { get }
```

```objc
@property (copy, readonly, nullable) NSImage * iconImage;
```

## See Also

### Accessing Group Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media group.
- [var name: String?](./name.md)
  The name of the media group.
- [var url: URL?](./url.md)
  The location of the media group.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/iconimage)*