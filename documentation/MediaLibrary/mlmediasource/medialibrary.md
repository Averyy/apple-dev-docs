# mediaLibrary

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A pointer to the media library instance that loaded this media source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }
```

```objc
@property (assign, readonly, nullable) MLMediaLibrary * mediaLibrary;
```

## See Also

### Identifying the Source
- [var mediaSourceIdentifier: String](./mediasourceidentifier.md)
  A unique identifier for the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/medialibrary)*