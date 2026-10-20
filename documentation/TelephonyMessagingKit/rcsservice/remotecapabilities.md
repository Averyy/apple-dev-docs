# RCSService.RemoteCapabilities

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing the capabilities of a remote handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RemoteCapabilities
```

## Topics

### Accessing handle metadata
- [let alternativeHandles: [RCSHandle]](./remotecapabilities/alternativehandles.md)
  Alternative handles for remote end.
- [enum RCSHandle](../rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](./remotecapabilities/isbusinesshandle.md)
  Whether remote end is a business handle.
### Accessing feature support
- [let supportsChat: Bool](./remotecapabilities/supportschat.md)
  Whether remote end supports chat.
- [let supportsFileTransfer: Bool](./remotecapabilities/supportsfiletransfer.md)
  Whether remote end supports file transfer.
- [let supportsGeolocation: Bool](./remotecapabilities/supportsgeolocation.md)
  Whether remote end supports geolocation.
### Accessing availability
- [let availability: RCSService.RemoteCapabilities.Availability?](./remotecapabilities/availability-swift.property.md)
  Availability of remote end.
- [RCSService.RemoteCapabilities.Availability](./remotecapabilities/availability-swift.enum.md)
  Enumeration indicating the availability of the remote end.
### Determining capability validity
- [let validUntil: Date?](./remotecapabilities/validuntil.md)
  Expiration date for the contained capabilities.
### Supporting RCS encryption
- [let supportsEndToEndEncryption: Bool](./remotecapabilities/supportsendtoendencryption.md)
  A Boolean value indicating whether the remote end supports end-to-end encryption.
### Instance Properties
- [let supportsExtendedMessagingCustomReaction: Bool](./remotecapabilities/supportsextendedmessagingcustomreaction.md)
  Whether remote end supports extended messaging custom reaction feature.
- [let supportsExtendedMessagingReaction: Bool](./remotecapabilities/supportsextendedmessagingreaction.md)
  Whether remote end supports extended messaging reaction feature.
- [let supportsExtendedMessagingReply: Bool](./remotecapabilities/supportsextendedmessagingreply.md)
  Whether remote end supports extended messaging reply feature.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Discovering remote capabilities
- [func remoteCapabilities(for: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?](./remotecapabilities%28for%29.md)
  Requests remote capability discovery for a given handle
- [RCSService.RemoteCapabilitiesRequest](./remotecapabilitiesrequest.md)
  A structure representing a request to retrieve the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities)*