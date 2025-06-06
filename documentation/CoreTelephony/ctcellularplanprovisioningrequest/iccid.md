# iccid

**Framework**: Core Telephony  
**Kind**: property

The provisioning request’s Integrated Circuit Card Identifier (ICCID).

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var iccid: String? { get set }
```

#### Discussion

This property is optional.

## See Also

- [var address: String](ctcellularplanprovisioningrequest/address.md)
  The address of the carrier network’s eSIM server.
- [var confirmationCode: String?](ctcellularplanprovisioningrequest/confirmationcode.md)
  The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.
- [var eid: String?](ctcellularplanprovisioningrequest/eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var matchingID: String?](ctcellularplanprovisioningrequest/matchingid.md)
  The provisioning request’s matching identifier (MatchingID).
- [var oid: String?](ctcellularplanprovisioningrequest/oid.md)
  The provisioning request’s Object Identifier (OID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/iccid)*