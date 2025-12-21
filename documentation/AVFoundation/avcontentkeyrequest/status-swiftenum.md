# AVContentKeyRequest.Status

**Framework**: AVFoundation  
**Kind**: enum

The status for a content key request.

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
enum Status
```

## Topics

### Request status
- [AVContentKeyRequest.Status.cancelled](avcontentkeyrequest/status-swift.enum/cancelled.md)
  The key request was canceled.
- [AVContentKeyRequest.Status.failed](avcontentkeyrequest/status-swift.enum/failed.md)
  The key request failed.
- [AVContentKeyRequest.Status.receivedResponse](avcontentkeyrequest/status-swift.enum/receivedresponse.md)
  The key request was received, and the key is in use.
- [AVContentKeyRequest.Status.renewed](avcontentkeyrequest/status-swift.enum/renewed.md)
  The key request was renewed.
- [AVContentKeyRequest.Status.requestingResponse](avcontentkeyrequest/status-swift.enum/requestingresponse.md)
  The key request was just created.
- [AVContentKeyRequest.Status.retried](avcontentkeyrequest/status-swift.enum/retried.md)
  The key request was retried.
### Initializers
- [init?(rawValue: Int)](avcontentkeyrequest/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var identifier: (any Sendable)?](avcontentkeyrequest/identifier.md)
  The identifier for the content key.
- [var originatingRecipient: (any AVContentKeyRecipient)?](avcontentkeyrequest/originatingrecipient.md)
  The AVContentKeyRecipient which initiated this request, if any.
- [var canProvidePersistableContentKey: Bool](avcontentkeyrequest/canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](avcontentkeyrequest/error.md)
  The error description for a failed key request.
- [var initializationData: Data?](avcontentkeyrequest/initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](avcontentkeyrequest/renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/status-swift.enum)*