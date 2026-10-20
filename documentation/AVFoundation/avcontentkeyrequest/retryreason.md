# AVContentKeyRequest.RetryReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVContentKeyRequestRetryReason;
```

## Topics

### Reasons for content key request retry
- [static let receivedObsoleteContentKey: AVContentKeyRequest.RetryReason](./retryreason/receivedobsoletecontentkey.md)
  An obsolete key response that was set on the previous content key request.
- [static let receivedResponseWithExpiredLease: AVContentKeyRequest.RetryReason](./retryreason/receivedresponsewithexpiredlease.md)
  A key response with an expired lease that was set on the previous content key request.
- [static let timedOut: AVContentKeyRequest.RetryReason](./retryreason/timedout.md)
  A key response that wasn’t set soon enough.
### Initializers
- [init(rawValue: String)](./retryreason/init%28rawvalue%29.md)
  Creates a retry reason with a string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a request
- [var contentKey: AVContentKey?](./contentkey.md)
  The generated content key.
- [var contentKeySpecifier: AVContentKeySpecifier](./contentkeyspecifier.md)
  The requested content key specifier.
- [var options: [String : any Sendable]](./options.md)
  A dictionary of options used to initialize key loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason)*