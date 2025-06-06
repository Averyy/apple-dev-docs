# AVContentKeyRequest.RetryReason

**Framework**: AVFoundation  
**Kind**: struct

The reason for asking the client to retry a content key request.

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
struct RetryReason
```

## Topics

### Reasons for Content Key Request Retry
- [static let receivedObsoleteContentKey: AVContentKeyRequest.RetryReason](avcontentkeyrequest/retryreason/receivedobsoletecontentkey.md)
  An obsolete key response that was set on the previous content key request.
- [static let receivedResponseWithExpiredLease: AVContentKeyRequest.RetryReason](avcontentkeyrequest/retryreason/receivedresponsewithexpiredlease.md)
  A key response with an expired lease that was set on the previous content key request.
- [static let timedOut: AVContentKeyRequest.RetryReason](avcontentkeyrequest/retryreason/timedout.md)
  A key response that wasn’t set soon enough.
### Initializers
- [init(rawValue: String)](avcontentkeyrequest/retryreason/init(rawvalue:).md)
  Creates a retry reason with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var contentKey: AVContentKey?](avcontentkeyrequest/contentkey.md)
  The generated content key.
- [var contentKeySpecifier: AVContentKeySpecifier](avcontentkeyrequest/contentkeyspecifier.md)
  The requested content key specifier.
- [var options: [String : any Sendable]](avcontentkeyrequest/options.md)
  A dictionary of options used to initialize key loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason)*