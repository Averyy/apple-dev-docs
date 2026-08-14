# CustomerEngagementSession.CustomerConfiguration

**Framework**: ProximityReader  
**Kind**: struct

A structure that contains configuration details for the connected customer device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct CustomerConfiguration
```

#### Overview

This is available on the [`CustomerEngagementSession.Event.ready`](customerengagementsession/event/ready.md) event after the merchant device establishes the peer connection with the customer’s device.

## Topics

### Instance Properties
- [let clientType: CustomerEngagementSession.PeerClientType](customerengagementsession/customerconfiguration-swift.struct/clienttype.md)
  An enum value that indicates the type of connected peer client.
- [let locale: Locale](customerengagementsession/customerconfiguration-swift.struct/locale.md)
  The customer’s current locale.
- [let sessionToken: CustomerEngagementSession.Token?](customerengagementsession/customerconfiguration-swift.struct/sessiontoken.md)
  The session token from the customer’s device.
- [let version: String](customerengagementsession/customerconfiguration-swift.struct/version.md)
  The engagement schema version of the connected customer device.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var customerConfiguration: CustomerEngagementSession.CustomerConfiguration?](customerengagementsession/customerconfiguration-swift.property.md)
  A structure containing configuration information of the customer device.
- [CustomerEngagementSession.PeerClientType](customerengagementsession/peerclienttype.md)
  A value that indicates the type of connected peer client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/customerconfiguration-swift.struct)*