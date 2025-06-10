# AVContentKeySystem

**Framework**: AVFoundation  
**Kind**: struct

A key-delivery method for a content key session.

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
struct AVContentKeySystem
```

## Topics

### Key-Delivery Methods
- [static let fairPlayStreaming: AVContentKeySystem](avcontentkeysystem/fairplaystreaming.md)
  A method of key delivery that uses FairPlay Streaming.
- [static let clearKey: AVContentKeySystem](avcontentkeysystem/clearkey.md)
  A method of key delivery that uses a clear key system.
- [static let authorizationToken: AVContentKeySystem](avcontentkeysystem/authorizationtoken.md)
  A method of key delivery that uses a token to authorize playback.
### Initializers
- [init(rawValue: String)](avcontentkeysystem/init(rawvalue:).md)
  Creates a content key system with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var keySystem: AVContentKeySystem](avcontentkeysession/keysystem.md)
  The type of key system used to retrieve keys.
- [var storageURL: URL?](avcontentkeysession/storageurl.md)
  A URL that points to a writable storage directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysystem)*