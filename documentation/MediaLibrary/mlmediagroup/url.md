# url

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The location of the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * URL;
```

#### Discussion

Some groups do not have a URL, in which case this returns `nil`. For example, a group that represents a filesystem folder on disk has a URL, but a group that represents a named face in iPhoto does not.

## See Also

### Accessing Group Attributes
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of attributes describing the media group.
- [var name: String?](./name.md)
  The name of the media group.
- [var iconImage: NSImage?](./iconimage.md)
  The media group’s icon.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/url)*