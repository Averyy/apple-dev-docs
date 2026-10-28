# CustomerEngagementSession.CustomerConfiguration

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A structure that contains configuration details for the connected customer device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct CustomerConfiguration
```

## Overview

This is available on the [`CustomerEngagementSession.Event.ready`](./event/ready.md) event after the merchant device establishes the peer connection with the customer’s device.

## Topics

### Instance Properties
- [let clientType: CustomerEngagementSession.PeerClientType](./customerconfiguration-swift.struct/clienttype.md)
  An enum value that indicates the type of connected peer client.
- [let locale: Locale](./customerconfiguration-swift.struct/locale.md)
  The customer’s current locale.
- [let sessionToken: CustomerEngagementSession.Token?](./customerconfiguration-swift.struct/sessiontoken.md)
  The session token from the customer’s device.
- [let version: String](./customerconfiguration-swift.struct/version.md)
  The engagement schema version of the connected customer device.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting customer configuration
- [var customerConfiguration: CustomerEngagementSession.CustomerConfiguration?](./customerconfiguration-swift.property.md)
  A structure containing configuration information of the customer device.
- [CustomerEngagementSession.PeerClientType](./peerclienttype.md)
  A value that indicates the type of connected peer client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/customerconfiguration-swift.struct)*