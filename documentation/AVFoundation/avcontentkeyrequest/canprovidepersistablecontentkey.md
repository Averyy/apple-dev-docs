# canProvidePersistableContentKey

**Framework**: AVFoundation  
**Kind**: property

The content key request used to create a persistable content key or respond to a previous request with a persistable content key.

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
var canProvidePersistableContentKey: Bool { get }
```

#### Discussion

The value of this property is automatically set to `YES` when the receiver is provided to the content key session’s delegate via the [`contentKeySession(_:didProvide:)`](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz.md) method. When this property is set to `YES`, the [`persistableContentKey(fromKeyVendorResponse:options:)`](avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse:options:).md) method can be used to create a persistable content key from the response.

When this property is set to `NO` and there is a request for a persistable content key, send the [`respondByRequestingPersistableContentKeyRequest()`](avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest().md) method.

## See Also

- [var identifier: (any Sendable)?](avcontentkeyrequest/identifier.md)
  The identifier for the content key.
- [var error: (any Error)?](avcontentkeyrequest/error.md)
  The error description for a failed key request.
- [var initializationData: Data?](avcontentkeyrequest/initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](avcontentkeyrequest/renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canprovidepersistablecontentkey)*