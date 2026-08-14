# CTCellularPlanProvisioningRequest

**Framework**: Core Telephony  
**Kind**: class

A request specifying an eSIM to download and install.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCellularPlanProvisioningRequest
```

#### Overview

You must set the [`address`](ctcellularplanprovisioningrequest/address.md) property for the request to be valid. All other properties are optional.

This class is only available to carrier apps with suitable entitlements.

## Topics

### Specifying Request Properties
- [var address: String](ctcellularplanprovisioningrequest/address.md)
  The address of the carrier network’s eSIM server.
- [var confirmationCode: String?](ctcellularplanprovisioningrequest/confirmationcode.md)
  The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.
- [var eid: String?](ctcellularplanprovisioningrequest/eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var iccid: String?](ctcellularplanprovisioningrequest/iccid.md)
  The provisioning request’s Integrated Circuit Card Identifier (ICCID).
- [var matchingID: String?](ctcellularplanprovisioningrequest/matchingid.md)
  The provisioning request’s matching identifier (MatchingID).
- [var oid: String?](ctcellularplanprovisioningrequest/oid.md)
  The provisioning request’s Object Identifier (OID).
### Initializers
- [init?(coder: NSCoder)](ctcellularplanprovisioningrequest/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CTCellularPlanProvisioning](ctcellularplanprovisioning.md)
  An object you use to download and install a carrier eSIM.
- [class CTCellularPlanProperties](ctcellularplanproperties.md)
  An object you use for an eSIM.
- [enum CTCellularPlanCapability](ctcellularplancapability.md)
  The type of cellular plan available for an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest)*