# keySystem

**Framework**: AVFoundation  
**Kind**: property

The type of key system used to retrieve keys.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var keySystem: AVContentKeySystem { get }
```

#### Discussion

Valid values for keySystem are [`fairPlayStreaming`](avcontentkeysystem/fairplaystreaming.md) and [`clearKey`](avcontentkeysystem/clearkey.md).

## See Also

- [struct AVContentKeySystem](avcontentkeysystem.md)
  A key-delivery method for a content key session.
- [var storageURL: URL?](avcontentkeysession/storageurl.md)
  A URL that points to a writable storage directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/keysystem)*