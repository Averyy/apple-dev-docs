# mediaSourceIdentifier

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the media source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var mediaSourceIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * mediaSourceIdentifier;
```

#### Discussion

For a list of possible media source identifiers, see [Media Source Identifiers](../media-source-identifiers.md).

## See Also

### Identifying the Source
- [var mediaLibrary: MLMediaLibrary?](./medialibrary.md)
  A pointer to the media library instance that loaded this media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/mediasourceidentifier)*