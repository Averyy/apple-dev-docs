# modificationDate

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The date and time when the media group was last altered.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var modificationDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * modificationDate;
```

## See Also

### Accessing Group Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media group.
- [var name: String?](./name.md)
  The name of the media group.
- [var iconImage: NSImage?](./iconimage.md)
  The media group’s icon.
- [var url: URL?](./url.md)
  The location of the media group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/modificationdate)*