# RCSService.RemoteCapabilities

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing the capabilities of a remote handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct RemoteCapabilities
```

## Topics

### Accessing handle metadata
- [let alternativeHandles: [RCSHandle]](rcsservice/remotecapabilities/alternativehandles.md)
  Alternative handles for remote end.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](rcsservice/remotecapabilities/isbusinesshandle.md)
  Whether remote end is a business handle.
### Accessing feature support
- [let supportsChat: Bool](rcsservice/remotecapabilities/supportschat.md)
  Whether remote end supports chat.
- [let supportsFileTransfer: Bool](rcsservice/remotecapabilities/supportsfiletransfer.md)
  Whether remote end supports file transfer.
- [let supportsGeolocation: Bool](rcsservice/remotecapabilities/supportsgeolocation.md)
  Whether remote end supports geolocation.
### Accessing availability
- [let availability: RCSService.RemoteCapabilities.Availability?](rcsservice/remotecapabilities/availability-swift.property.md)
  Availability of remote end.
- [RCSService.RemoteCapabilities.Availability](rcsservice/remotecapabilities/availability-swift.enum.md)
  Enumeration indicating the availability of the remote end.
### Determining capability validity
- [let validUntil: Date?](rcsservice/remotecapabilities/validuntil.md)
  Expiration date for the contained capabilities.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/remotecapabilities/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/remotecapabilities/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing remote capabilities
- [static func == (RCSService.RemoteCapabilities, RCSService.RemoteCapabilities) -> Bool](rcsservice/remotecapabilities/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/remotecapabilities/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func remoteCapabilities(for: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?](rcsservice/remotecapabilities(for:).md)
  Requests remote capability discovery for a given handle
- [RCSService.RemoteCapabilitiesRequest](rcsservice/remotecapabilitiesrequest.md)
  A structure representing a request to retrieve the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities)*