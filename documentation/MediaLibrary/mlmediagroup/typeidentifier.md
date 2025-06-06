# typeIdentifier

**Framework**: Media Library  
**Kind**: property

An identifier for the media group’s type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var typeIdentifier: String { get }
```

#### Discussion

Multiple groups within a media source can have the same type identifier. For descriptions of group type identifiers, see [`MediaLibrary Constants`](medialibrary-constants.md).

## See Also

- [var identifier: String](mlmediagroup/identifier.md)
  An identifier for the media group.
- [var mediaSourceIdentifier: String](mlmediagroup/mediasourceidentifier.md)
  An identifier for the source that loaded the media group.
- [var mediaLibrary: MLMediaLibrary?](mlmediagroup/medialibrary.md)
  A pointer to the media library instance that loaded the media group’s source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/typeidentifier)*