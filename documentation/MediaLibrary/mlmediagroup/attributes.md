# attributes

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A dictionary of attributes describing the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var attributes: [String : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * attributes;
```

#### Discussion

These attributes are usually defined by the source app, such as iTunes. For example, an iTunes playlist is represented as a group. iTunes attaches attributes such as “Playlist Persistent ID” to the group in its `attributes`. The attribute names vary based on the media source. Attributes common to all sources are called out as separate properties.

## See Also

### Accessing Group Attributes
- [var name: String?](./name.md)
  The name of the media group.
- [var iconImage: NSImage?](./iconimage.md)
  The media group’s icon.
- [var url: URL?](./url.md)
  The location of the media group.
- [var modificationDate: Date?](./modificationdate.md)
  The date and time when the media group was last altered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/attributes)*