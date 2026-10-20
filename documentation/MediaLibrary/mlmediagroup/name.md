# name

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The name of the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var name: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * name;
```

#### Discussion

This string is human-readable. It is either user created (such as the name of an iTunes playlist) or already localized.

## See Also

### Accessing Group Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media group.
- [var iconImage: NSImage?](./iconimage.md)
  The media group’s icon.
- [var url: URL?](./url.md)
  The location of the media group.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/name)*