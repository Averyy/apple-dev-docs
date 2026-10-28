# identifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifier for the content key.

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
var identifier: (any Sendable)? { get }
```

```objc
@property (readonly, nullable) id identifier;
```

## Discussion

This property is specific to the container and the protocol. To use the key with an HTTP Live Streaming [`AVURLAsset`](../avurlasset.md), the identifier must be an [`NSURL`](../../Foundation/nsurl.md) that matches a key `URI` in the media playlist.

## See Also

### Getting content key request properties
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
- [AVContentKeyRequest.Status](./status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/identifier)*