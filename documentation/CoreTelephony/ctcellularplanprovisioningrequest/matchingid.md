# matchingID

**Framework**: Core Telephony  
**Kind**: property

The provisioning request’s matching identifier (MatchingID).

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var matchingID: String? { get set }
```

#### Discussion

See GSMA SGP.22 for description. This property is optional.

## See Also

- [var address: String](ctcellularplanprovisioningrequest/address.md)
  The address of the carrier network’s eSIM server.
- [var confirmationCode: String?](ctcellularplanprovisioningrequest/confirmationcode.md)
  The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.
- [var eid: String?](ctcellularplanprovisioningrequest/eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var iccid: String?](ctcellularplanprovisioningrequest/iccid.md)
  The provisioning request’s Integrated Circuit Card Identifier (ICCID).
- [var oid: String?](ctcellularplanprovisioningrequest/oid.md)
  The provisioning request’s Object Identifier (OID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/matchingid)*