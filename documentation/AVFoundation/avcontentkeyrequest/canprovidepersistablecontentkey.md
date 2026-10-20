# canProvidePersistableContentKey

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL canProvidePersistableContentKey;
```

#### Discussion

The value of this property is automatically set to `YES` when the receiver is provided to the content key session’s delegate via the [`contentKeySession(_:didProvide:)`](../avcontentkeysessiondelegate/contentkeysession%28_,didprovide%29-2wdgz.md) method. When this property is set to `YES`, the [`persistableContentKey(fromKeyVendorResponse:options:)`](../avpersistablecontentkeyrequest/persistablecontentkey%28fromkeyvendorresponse,options%29.md) method can be used to create a persistable content key from the response.

When this property is set to `NO` and there is a request for a persistable content key, send the [`respondByRequestingPersistableContentKeyRequest()`](./respondbyrequestingpersistablecontentkeyrequest%28%29.md) method.

## See Also

### Getting content key request properties
- [var identifier: (any Sendable)?](./identifier.md)
  The identifier for the content key.
- [var originatingRecipient: (any AVContentKeyRecipient)?](./originatingrecipient.md)
  The AVContentKeyRecipient which initiated this request, if any.
- [var error: (any Error)?](./error.md)
  The error description for a failed key request.
- [var initializationData: Data?](./initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](./renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](./status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](./status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canprovidepersistablecontentkey)*