# renewsExpiringResponseData

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the content key request renews previously provided response data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var renewsExpiringResponseData: Bool { get }
```

#### Discussion

The value of this property is `YES` if the request renews previously provided response data that is expiring or has already expired.

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
- [var status: AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/renewsexpiringresponsedata)*