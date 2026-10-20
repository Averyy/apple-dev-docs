# AVContentKeyRequest.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVContentKeyRequestStatus : NSInteger;
```

## Topics

### Request status
- [AVContentKeyRequest.Status.cancelled](./status-swift.enum/cancelled.md)
  The key request was canceled.
- [AVContentKeyRequest.Status.failed](./status-swift.enum/failed.md)
  The key request failed.
- [AVContentKeyRequest.Status.receivedResponse](./status-swift.enum/receivedresponse.md)
  The key request was received, and the key is in use.
- [AVContentKeyRequest.Status.renewed](./status-swift.enum/renewed.md)
  The key request was renewed.
- [AVContentKeyRequest.Status.requestingResponse](./status-swift.enum/requestingresponse.md)
  The key request was just created.
- [AVContentKeyRequest.Status.retried](./status-swift.enum/retried.md)
  The key request was retried.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting content key request properties
- [var identifier: (any Sendable)?](./identifier.md)
  The identifier for the content key.
- [var originatingRecipient: (any AVContentKeyRecipient)?](./originatingrecipient.md)
  The AVContentKeyRecipient which initiated this request, if any.
- [var canProvidePersistableContentKey: Bool](./canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](./error.md)
  The error description for a failed key request.
- [var initializationData: Data?](./initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](./renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](./status-swift.property.md)
  The current state of the content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/status-swift.enum)*