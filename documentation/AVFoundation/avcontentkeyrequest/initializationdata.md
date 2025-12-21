# initializationData

**Framework**: AVFoundation  
**Kind**: property

The data used to obtain a key response.

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
var initializationData: Data? { get }
```

#### Discussion

This property is specific to the container and the protocol.

## See Also

- [var identifier: (any Sendable)?](avcontentkeyrequest/identifier.md)
  The identifier for the content key.
- [var originatingRecipient: (any AVContentKeyRecipient)?](avcontentkeyrequest/originatingrecipient.md)
  The AVContentKeyRecipient which initiated this request, if any.
- [var canProvidePersistableContentKey: Bool](avcontentkeyrequest/canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](avcontentkeyrequest/error.md)
  The error description for a failed key request.
- [var renewsExpiringResponseData: Bool](avcontentkeyrequest/renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/initializationdata)*