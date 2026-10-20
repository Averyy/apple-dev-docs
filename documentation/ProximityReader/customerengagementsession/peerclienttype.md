# CustomerEngagementSession.PeerClientType

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

A value that indicates the type of connected peer client.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum PeerClientType
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.PeerClientType.localWireless](./peerclienttype/localwireless.md)
  This case indicates a peer client connection using a direct local wireless connection.
- [CustomerEngagementSession.PeerClientType.none](./peerclienttype/none.md)
  This case indicates no peer client connection.
- [CustomerEngagementSession.PeerClientType.web](./peerclienttype/web.md)
  This case indicates a peer web application client connection via a server relay.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting customer configuration
- [CustomerEngagementSession.CustomerConfiguration](./customerconfiguration-swift.struct.md)
  A structure that contains configuration details for the connected customer device.
- [var customerConfiguration: CustomerEngagementSession.CustomerConfiguration?](./customerconfiguration-swift.property.md)
  A structure containing configuration information of the customer device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/peerclienttype)*