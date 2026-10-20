# receivedResponseWithExpiredLease

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A key response with an expired lease that was set on the previous content key request.

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
static let receivedResponseWithExpiredLease: AVContentKeyRequest.RetryReason
```

```c
extern AVContentKeyRequestRetryReason const AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease;
```

## See Also

### Reasons for content key request retry
- [static let receivedObsoleteContentKey: AVContentKeyRequest.RetryReason](./receivedobsoletecontentkey.md)
  An obsolete key response that was set on the previous content key request.
- [static let timedOut: AVContentKeyRequest.RetryReason](./timedout.md)
  A key response that wasn’t set soon enough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason/receivedresponsewithexpiredlease)*