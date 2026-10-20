# mediaLibrary

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A pointer to the media library instance that loaded the media object’s source.

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

### Identifying the Object
- [var identifier: String](./identifier.md)
  An identifier for the media object.
- [var mediaSourceIdentifier: String](./mediasourceidentifier.md)
  An identifier for the source that loaded the media object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediaobject/medialibrary)*