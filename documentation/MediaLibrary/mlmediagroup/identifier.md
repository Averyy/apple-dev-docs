# identifier

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

An identifier for the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (copy, readonly) NSString * identifier;
```

## Discussion

Each group’s identifier is unique within a media source.

## See Also

### Identifying the Group
- [var typeIdentifier: String](./typeidentifier.md)
  An identifier for the media group’s type.
- [var mediaSourceIdentifier: String](./mediasourceidentifier.md)
  An identifier for the source that loaded the media group.
- [var mediaLibrary: MLMediaLibrary?](./medialibrary.md)
  A pointer to the media library instance that loaded the media group’s source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/identifier)*