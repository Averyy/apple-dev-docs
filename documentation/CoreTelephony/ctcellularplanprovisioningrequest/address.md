# address

**Framework**: Core Telephony  
**Kind**: property

The address of the carrier network’s eSIM server.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var address: String { get set }
```

#### Discussion

The destination server must support the SMDP+ standard.

You must set this property for the request to be valid.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/address)*